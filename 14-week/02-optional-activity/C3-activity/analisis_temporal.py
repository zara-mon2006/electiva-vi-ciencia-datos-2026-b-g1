"""Corte 3 · Semana 14 — Análisis temporal y visualización (producción de septiembre, 3 máquinas).

Fuente: data/produccion_septiembre.csv (taller de la semana 8; datos ficticios, 1-15 sep 2026).
Serie principal: unidades producidas por máquina y por día (promedio de las máquinas con dato válido).

Uso:  python analisis_temporal.py      (desde esta carpeta)
"""
import re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

AQUI = Path(__file__).resolve().parent
IMG, SAL = AQUI / "img", AQUI / "salidas"
IMG.mkdir(exist_ok=True)
SAL.mkdir(exist_ok=True)

# ---------------------------------------------------------------- 1. Limpieza (reglas explícitas)
raw = pd.read_csv(AQUI / "data" / "produccion_septiembre.csv")
df = raw.copy()
df["maquina"] = df["maquina"].str.strip().str.upper().str.replace(r"^M-?(\d)(\d)$", r"M-\1\2", regex=True)
assert set(df["maquina"]) == {"M-01", "M-02", "M-03"}
n_dup = int(df.duplicated().sum())
df = df.drop_duplicates().reset_index(drop=True)                      # 2 filas repetidas
df["fecha"] = pd.to_datetime(df["fecha"])
assert len(df) == 45 and not df.duplicated(["fecha", "maquina"]).any()  # 15 días x 3 máquinas
UMBRAL = 5000                                                           # lo normal ronda 800-1 100
n_atip = int((df["unidades_producidas"] > UMBRAL).sum())
n_neg = int((df["unidades_defectuosas"] < 0).sum())
df.loc[df["unidades_producidas"] > UMBRAL, "unidades_producidas"] = np.nan   # 11 600: error de captura (no se corrige a ojo)
df.loc[df["unidades_defectuosas"] < 0, "unidades_defectuosas"] = np.nan      # -4 defectuosas: imposible
valido = df["unidades_producidas"].notna() & df["unidades_defectuosas"].notna()   # filas aptas para tasas de defecto
df.to_csv(SAL / "produccion_limpia.csv", index=False)

# ---------------------------------------------------------------- 2. Resample + media móvil
s = df.set_index("fecha")
diario = s.resample("D").agg(unidades_por_maquina=("unidades_producidas", "mean"),
                             maquinas_validas=("unidades_producidas", "count"))
diario["media_movil_3d"] = diario["unidades_por_maquina"].rolling(3).mean()
tmp = s[valido.to_numpy()].resample("D").agg(defectuosas=("unidades_defectuosas", "sum"), producidas=("unidades_producidas", "sum"))
diario["pct_defectos"] = 100 * tmp["defectuosas"] / tmp["producidas"]
diario["temperatura_media_c"] = s["temperatura_c"].resample("D").mean()
diario.to_csv(SAL / "serie_diaria.csv", index_label="fecha")

semanal = s.resample("W-SUN").agg(dias=("maquina", lambda x: x.index.nunique()),
                                  unidades_por_maquina=("unidades_producidas", "mean"))
semanal.to_csv(SAL / "serie_semanal.csv", index_label="semana_termina")
assert len(diario) == 15 and (diario["maquinas_validas"] >= 2).all()

# ---------------------------------------------------------------- 3. Tendencia
y = diario["unidades_por_maquina"]
x = np.arange(len(y))
reg = stats.linregress(x, y)
media, sd = y.mean(), y.std()
mm = diario["media_movil_3d"].dropna()
cv = 100 * sd / media

# ---------------------------------------------------------------- 4. Estacionalidad (solo 15 días ≈ 2 ciclos semanales)
resid = y - (reg.intercept + reg.slope * x)
acf7 = resid.autocorr(7)
por_dia = y.groupby(y.index.dayofweek).mean()
nombres = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
kw = stats.kruskal(*[g.to_numpy() for _, g in y.groupby(y.index.dayofweek)])

# ---------------------------------------------------------------- 5. Comparación por máquina: tasa de defectos con IC de Wilson 95 %
def wilson(k, n, z=1.96):
    p = k / n
    c = (p + z * z / (2 * n)) / (1 + z * z / n)
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return 100 * (c - h), 100 * (c + h)

v = df[valido]
maq = v.groupby("maquina").agg(producidas=("unidades_producidas", "sum"), defectuosas=("unidades_defectuosas", "sum"),
                               dias=("fecha", "nunique"), temp=("temperatura_c", "mean"))
maq["pct_defectos"] = 100 * maq["defectuosas"] / maq["producidas"]
maq[["ic_inf", "ic_sup"]] = [wilson(k, n) for k, n in zip(maq["defectuosas"], maq["producidas"])]
maq["unidades_por_dia"] = df.groupby("maquina")["unidades_producidas"].mean()
chi = stats.chi2_contingency(np.array([maq["defectuosas"], maq["producidas"] - maq["defectuosas"]]))
maq.to_csv(SAL / "comparacion_por_maquina.csv", index_label="maquina")
razon = maq.loc["M-03", "pct_defectos"] / maq.drop("M-03")["pct_defectos"].mean()
peor = maq["pct_defectos"].idxmax()
assert peor == "M-03"

# ---------------------------------------------------------------- 6. Gráficos
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
AZUL, GRIS, NAR = "#1f5fa8", "#9aa5b1", "#d9822b"

# Gráfico 1 — evolución (línea; eje Y desde 0)
assert reg.pvalue > 0.05                                  # el título afirma "sin tendencia"
fig, ax = plt.subplots(figsize=(9, 4.6))
ax.plot(diario.index, y, color=GRIS, marker="o", ms=4, lw=1.3, label="Unidades por máquina (promedio diario)")
ax.plot(diario.index, diario["media_movil_3d"], color=AZUL, lw=2.8, label="Media móvil de 3 días")
ax.axhline(media, color="#555", lw=1, ls="--", label=f"Promedio del periodo ({media:,.0f})".replace(",", " "))
ax.set_ylim(0, 1400)
ax.set_ylabel("Unidades por máquina y por día")
ax.set_xlabel("Día (septiembre de 2026)")
ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d"))
ax.xaxis.set_major_locator(matplotlib.dates.DayLocator(interval=1))
ax.set_title(f"La producción diaria por máquina se mantuvo estable en torno a {round(media, -1):.0f} unidades\n"
             "entre el 1 y el 15 de septiembre, sin tendencia clara", loc="left", fontsize=11, fontweight="bold")
ax.legend(frameon=False, loc="lower right", fontsize=8.5)
ax.grid(axis="y", alpha=.25)
fig.text(0.01, 0.005, "Fuente: produccion_septiembre.csv (datos ficticios, 45 registros tras limpiar). Se excluyó el dato de 11 600 unidades (M-01, 7 sep). Eje Y desde 0.",
         fontsize=7.5, color="#555")
fig.tight_layout(rect=(0, 0.03, 1, 1))
fig.savefig(IMG / "g1_evolucion_diaria.png", dpi=170)
plt.close(fig)

# Gráfico 2 — comparación (barras con IC de Wilson; eje Y desde 0)
fig, ax = plt.subplots(figsize=(9, 4.6))
orden = list(maq.index)
cols = [NAR if m == "M-03" else GRIS for m in orden]
err = [maq["pct_defectos"] - maq["ic_inf"], maq["ic_sup"] - maq["pct_defectos"]]
ax.bar(orden, maq["pct_defectos"], color=cols, width=0.55, yerr=err, capsize=5, ecolor="#333")
for i, m in enumerate(orden):
    ax.text(i, maq.loc[m, "ic_sup"] + 0.25, f"{maq.loc[m, 'pct_defectos']:.1f} %".replace(".", ","), ha="center", fontweight="bold", fontsize=10)
ax.set_xticks(range(3), [f"{m}\nTemp. media " + f"{maq.loc[m, 'temp']:.1f}".replace(".", ",") + " °C" for m in orden])
ax.set_ylim(0, 8)
ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(decimals=0))
ax.set_ylabel("Unidades defectuosas (% de lo producido)")
otras = maq.drop("M-03")["pct_defectos"]
fmt = lambda x: f"{x:.1f}".replace(".", ",")
ax.set_title(f"M-03 tiene {fmt(razon)} veces más defectos que las otras dos máquinas\n"
             f"({fmt(maq.loc['M-03', 'pct_defectos'])} % frente a {fmt(otras.min())}–{fmt(otras.max())} %)",
             loc="left", fontsize=11, fontweight="bold")
ax.grid(axis="y", alpha=.25)
fig.text(0.01, 0.005, "Fuente: produccion_septiembre.csv. Barras de error = intervalo de confianza de Wilson al 95 %. Excluye 2 registros inválidos (11 600 u.; -4 defectuosas). Eje Y desde 0.",
         fontsize=7.5, color="#555")
fig.tight_layout(rect=(0, 0.03, 1, 1))
fig.savefig(IMG / "g2_comparacion_maquinas.png", dpi=170)
plt.close(fig)

# ---------------------------------------------------------------- 7. Resumen
res = f"""# Resultados del análisis temporal (generado por analisis_temporal.py)

Periodo: {diario.index[0].date()} a {diario.index[-1].date()} · {len(diario)} días · 3 máquinas · {len(df)} registros tras limpiar
Limpieza: {len(raw)} filas crudas → {n_dup} duplicados eliminados · nombres de máquina normalizados · {n_atip} dato atípico (>{UMBRAL}) y {n_neg} defectuosas negativas → vacío

## Tendencia (unidades por máquina y por día)
- Promedio: {media:.1f} · desv. estándar: {sd:.1f} ({cv:.1f} % del promedio) · mín {y.min():.1f} ({y.idxmin().date()}) · máx {y.max():.1f} ({y.idxmax().date()})
- Pendiente lineal: {reg.slope:+.2f} unidades/día (IC 95 %: {reg.slope - stats.t.ppf(.975, len(y)-2)*reg.stderr:+.2f} a {reg.slope + stats.t.ppf(.975, len(y)-2)*reg.stderr:+.2f}); R² = {reg.rvalue**2:.3f}; p = {reg.pvalue:.2f}
- Media móvil 3 d: máximo {mm.max():.1f} ({mm.idxmax().date()}) · mínimo {mm.min():.1f} ({mm.idxmin().date()})

## Resample semanal (W-SUN)
{semanal.round(1).to_string()}

## Estacionalidad
- Promedio por día de la semana: {', '.join(f'{nombres[d]} {v:.0f}' for d, v in por_dia.items())} · Kruskal-Wallis p = {kw.pvalue:.2f} (solo 2 observaciones por día)
- Autocorrelación al rezago 7 de la serie sin tendencia: {acf7:+.2f} (n = {len(resid) - 7} pares)

## Comparación por máquina (registros válidos)
{maq.round(2).to_string()}
chi-cuadrado defectos x máquina: p = {chi[1]:.2e} · M-03 / promedio de las otras dos = {razon:.1f}×
"""
(SAL / "resumen_resultados.md").write_text(res, encoding="utf-8")
print(res)
