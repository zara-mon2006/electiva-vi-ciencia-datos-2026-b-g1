# Resultados del análisis temporal (generado por analisis_temporal.py)

Periodo: 2026-09-01 a 2026-09-15 · 15 días · 3 máquinas · 45 registros tras limpiar
Limpieza: 47 filas crudas → 2 duplicados eliminados · nombres de máquina normalizados · 1 dato atípico (>5000) y 1 defectuosas negativas → vacío

## Tendencia (unidades por máquina y por día)
- Promedio: 993.3 · desv. estándar: 46.7 (4.7 % del promedio) · mín 885.7 (2026-09-13) · máx 1074.7 (2026-09-15)
- Pendiente lineal: -0.21 unidades/día (IC 95 %: -6.46 a +6.04); R² = 0.000; p = 0.94
- Media móvil 3 d: máximo 1016.8 (2026-09-10) · mínimo 938.2 (2026-09-13)

## Resample semanal (W-SUN)
            dias  unidades_por_maquina
fecha                                 
2026-09-06     6                 995.6
2026-09-13     7                 980.0
2026-09-20     2                1029.3

## Estacionalidad
- Promedio por día de la semana: Lun 994, Mar 1030, Mié 968, Jue 1030, Vie 957, Sáb 1010, Dom 945 · Kruskal-Wallis p = 0.22 (solo 2 observaciones por día)
- Autocorrelación al rezago 7 de la serie sin tendencia: +0.27 (n = 8 pares)

## Comparación por máquina (registros válidos)
         producidas  defectuosas  dias   temp  pct_defectos  ic_inf  ic_sup  unidades_por_dia
maquina                                                                                      
M-01        13980.0        271.0    14  33.08          1.94    1.72    2.18            998.57
M-02        14074.0        181.0    14  31.49          1.29    1.11    1.49           1013.27
M-03        14518.0        843.0    15  37.13          5.81    5.44    6.20            967.87
chi-cuadrado defectos x máquina: p = 6.64e-127 · M-03 / promedio de las otras dos = 3.6×
