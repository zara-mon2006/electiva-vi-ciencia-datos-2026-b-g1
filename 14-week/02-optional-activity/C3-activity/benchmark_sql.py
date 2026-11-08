"""Comprueba y mide las dos consultas de consultas_sql.sql en SQLite.

1) Verifica que ambas dan la misma media móvil que pandas (salidas/serie_diaria.csv).
2) Muestra el plan de ejecución (EXPLAIN QUERY PLAN) de cada una.
3) Mide el tiempo (mejor de 5) con las 45 filas reales y con una tabla ampliada (cada fila repetida
   2 000 veces = 90 000 filas; los promedios diarios no cambian, solo el volumen).

Uso:  python benchmark_sql.py      (desde esta carpeta; ejecutar antes analisis_temporal.py)
"""
import sqlite3
import time
from pathlib import Path

import pandas as pd

AQUI = Path(__file__).resolve().parent
sql = (AQUI / "consultas_sql.sql").read_text(encoding="utf-8")
ANTES = sql[sql.index("SELECT d.dia"):].split(";")[0] + ";"
DESPUES = sql[sql.index("WITH diario"):]

PANDAS = pd.read_csv(AQUI / "salidas" / "serie_diaria.csv")["media_movil_3d"].to_numpy()
df = pd.read_csv(AQUI / "salidas" / "produccion_limpia.csv")


def crear(replicas: int) -> sqlite3.Connection:
    con = sqlite3.connect(":memory:")
    pd.concat([df] * replicas, ignore_index=True).to_sql("produccion", con, index=False)
    return con


def tiempo(con, consulta, veces=5):
    mejor, filas = 1e9, None
    for _ in range(veces):
        t0 = time.perf_counter()
        filas = con.execute(consulta).fetchall()
        mejor = min(mejor, time.perf_counter() - t0)
    return mejor * 1000, filas


out = ["# Resultados SQL (generado por benchmark_sql.py)\n"]

# --- 1. Corrección
con = crear(1)
_, f_antes = tiempo(con, ANTES, 1)
_, f_desp = tiempo(con, DESPUES, 1)
mm_antes = [r[1] for r in f_antes]
mm_desp = [r[3] for r in f_desp]
assert len(mm_antes) == len(mm_desp) == len(PANDAS) == 15
ok_desp = all((a is None and pd.isna(b)) or (a is not None and abs(a - b) < 1e-9) for a, b in zip(mm_desp, PANDAS))
# La consulta "antes" no deja NULL en los 2 primeros días: se compara desde el 3.º.
ok_antes = all(abs(a - b) < 1e-9 for a, b in zip(mm_antes[2:], PANDAS[2:]))
out.append(f"## Corrección\n- Consulta DESPUÉS igual a pandas en los {len(PANDAS)} días: **{ok_desp}**\n"
           f"- Consulta ANTES igual a pandas desde el día 3 (los 2 primeros no tienen ventana completa): **{ok_antes}**\n")
assert ok_desp and ok_antes

# --- 2. Planes
out.append("## Plan de ejecución (EXPLAIN QUERY PLAN)\n")
for nombre, q in (("ANTES", ANTES), ("DESPUÉS", DESPUES)):
    plan = con.execute("EXPLAIN QUERY PLAN " + q.strip().rstrip(";")).fetchall()
    out.append(f"**{nombre}**\n```\n" + "\n".join(r[3] for r in plan) + "\n```\n")

# --- 3. Tiempos
out.append("## Tiempo (mejor de 5 ejecuciones, ms)\n\n| Tabla | Filas | ANTES | DESPUÉS | Mejora |\n|---|---|---|---|---|")
for etiqueta, rep in (("Datos reales", 1), ("Ampliada ×2 000", 2000)):
    c = crear(rep)
    n = c.execute("SELECT COUNT(*) FROM produccion").fetchone()[0]
    t_a, _ = tiempo(c, ANTES)
    t_d, _ = tiempo(c, DESPUES)
    out.append(f"| {etiqueta} | {n:,} | {t_a:,.2f} | {t_d:,.2f} | {t_a / t_d:,.1f}× |")
out.append("\nNota: con las 45 filas reales ambas consultas son instantáneas; la diferencia solo importa a escala. Los tiempos dependen del equipo.")

texto = "\n".join(out) + "\n"
(AQUI / "salidas" / "resultados_sql.md").write_text(texto, encoding="utf-8")
print(texto)
