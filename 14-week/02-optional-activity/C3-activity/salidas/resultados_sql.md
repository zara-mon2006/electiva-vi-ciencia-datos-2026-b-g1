# Resultados SQL (generado por benchmark_sql.py)

## Corrección
- Consulta DESPUÉS igual a pandas en los 15 días: **True**
- Consulta ANTES igual a pandas desde el día 3 (los 2 primeros no tienen ventana completa): **True**

## Plan de ejecución (EXPLAIN QUERY PLAN)

**ANTES**
```
CO-ROUTINE d
SCAN produccion
USE TEMP B-TREE FOR DISTINCT
SCAN d
CORRELATED SCALAR SUBQUERY 2
CO-ROUTINE p
SCAN r
USE TEMP B-TREE FOR GROUP BY
SCAN p
USE TEMP B-TREE FOR ORDER BY
```

**DESPUÉS**
```
CO-ROUTINE (subquery-3)
CO-ROUTINE diario
SCAN produccion
USE TEMP B-TREE FOR GROUP BY
SCAN diario
USE TEMP B-TREE FOR ORDER BY
SCAN (subquery-3)
```

## Tiempo (mejor de 5 ejecuciones, ms)

| Tabla | Filas | ANTES | DESPUÉS | Mejora |
|---|---|---|---|---|
| Datos reales | 45 | 0.15 | 0.02 | 6.7× |
| Ampliada ×2 000 | 90,000 | 279.09 | 21.65 | 12.9× |

Nota: con las 45 filas reales ambas consultas son instantáneas; la diferencia solo importa a escala. Los tiempos dependen del equipo.
