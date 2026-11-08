-- Corte 3 · Semana 14 — Unidades por máquina y por día, con media móvil de 3 días (SQLite >= 3.25).
-- Tabla: produccion(fecha DATE, maquina TEXT, unidades_producidas REAL NULL, unidades_defectuosas REAL NULL, temperatura_c REAL NULL)
-- cargada desde salidas/produccion_limpia.csv (45 filas). AVG ignora los NULL (el dato de 11 600 se dejó vacío en la limpieza).
-- La media móvil es el promedio simple de los 3 promedios diarios, igual que rolling(3).mean() en pandas.

------------------------------------------------------------------------------
-- ANTES · Subconsulta correlacionada sobre la tabla cruda
-- Para cada día vuelve a leer y agrupar todas las filas de su ventana de 3 días, y aplica
-- date() a la columna dentro del WHERE (no puede usar índices).
-- Costo ≈ (n.º de días × 3) × (n.º de filas).
------------------------------------------------------------------------------
SELECT d.dia,
       (SELECT AVG(p.promedio)
          FROM (SELECT date(r.fecha) AS dia, AVG(r.unidades_producidas) AS promedio
                  FROM produccion r
                 WHERE date(r.fecha) BETWEEN date(d.dia, '-2 days') AND d.dia
                 GROUP BY 1) AS p) AS media_movil_3d
  FROM (SELECT DISTINCT date(fecha) AS dia FROM produccion) AS d
 ORDER BY d.dia;

------------------------------------------------------------------------------
-- DESPUÉS · Agregar una sola vez y usar una función de ventana
-- 1) Una CTE promedia por día en un único recorrido de la tabla (O(n)).
-- 2) AVG(...) OVER (ROWS 2 PRECEDING) promedia sobre ~15 filas diarias, no sobre todas las filas.
-- 3) El CASE deja NULL los 2 primeros días (ventana incompleta), igual que rolling(3) en pandas.
------------------------------------------------------------------------------
WITH diario AS (
    SELECT date(fecha)                  AS dia,
           AVG(unidades_producidas)     AS unidades_por_maquina,
           COUNT(unidades_producidas)   AS maquinas_validas
      FROM produccion
     GROUP BY 1
)
SELECT dia, unidades_por_maquina, maquinas_validas,
       CASE WHEN COUNT(*) OVER w = 3 THEN AVG(unidades_por_maquina) OVER w END AS media_movil_3d
  FROM diario
WINDOW w AS (ORDER BY dia ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)
 ORDER BY dia;
