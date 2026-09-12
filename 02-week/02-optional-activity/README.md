# Clasificación de Datos y Análisis de las V del Big Data: Mercado Bursátil de Tokio (JPX)

**Semana 2 — Ciencia de Datos | Corte 1 | Actividad formativa (opcional, sin nota)**

![Kaggle](https://img.shields.io/badge/Kaggle-JPX_Dataset-20BEFF?style=flat-square&logo=kaggle)
![Big Data](https://img.shields.io/badge/Big_Data-5_V's-blue?style=flat-square)
![Data](https://img.shields.io/badge/Entrega-GitHub-black?style=flat-square&logo=github)
![IEEE](https://img.shields.io/badge/Referencias-Formato_IEEE-orange?style=flat-square)

---

## 📌 Descripción

Segunda etapa del proyecto de ciencia de datos aplicado al mercado bursátil de Tokio. Este documento amplía el inventario de datos a **7 fuentes**, clasificándolas según su nivel de estructura, evalúa la relevancia de las cinco V del Big Data para el proyecto, y señala un problema concreto de veracidad (calidad) junto con la estrategia para detectarlo.

> 📄 El desarrollo completo (portada, abstract, marco teórico) está en `OPCIONAL ACTIVITY 02.pdf`, incluido en esta carpeta.

---

## 🎯 Objetivos

- **Listar** al menos seis fuentes de datos del proyecto, clasificándolas como estructuradas, semiestructuradas o no estructuradas.
- **Indicar** cuáles de las cinco V del Big Data son críticas para este proyecto y justificar por qué.
- **Señalar** un posible problema de veracidad (calidad) y describir cómo podría detectarse.

---

## 🗂️ Fuentes de datos y clasificación

| # | Fuente / Campo | Tipo de dato |
|---|---|---|
| 1 | `stock_prices.csv` | Estructurado |
| 2 | `financials.csv` | Estructurado |
| 3 | `options.csv` | Estructurado |
| 4 | `trades.csv` | Estructurado |
| 5 | `stock_list.csv` | Estructurado |
| 6 | Comunicados TDnet (TSE) | **Semiestructurado** |
| 7 | Noticias financieras Nikkei/NQN | **No estructurado** |

📎 Tabla completa con descripciones en `Fuentes_datos_Semana2.xlsx` (hoja **"Fuentes y clasificacion"**).

---

## 📈 V relevantes del Big Data

| V | ¿Crítica? | Justificación breve |
|---|---|---|
| Volumen | Media | ~2000 acciones × varios años de precios, financieros y opciones |
| Velocidad | Media | Actualización diaria/semanal; procesamiento *batch* suficiente |
| **Variedad** | **Alta** | Estructurado + semiestructurado (TDnet) + no estructurado (noticias) |
| **Veracidad** | **Alta** | Datos faltantes en reportes financieros y desalineación temporal entre fuentes |
| Valor | Alta | Impacto económico directo en decisiones de inversión |

📎 Análisis completo en `Fuentes_datos_Semana2.xlsx` (hoja **"V relevantes Big Data"**).

---

## ⚠️ Reto de veracidad

**Problema:** desalineación temporal y valores faltantes entre `financials.csv`, comunicados TDnet y `stock_prices.csv`.

**Detección:** validación de completitud (% de nulos por columna), validación cruzada de fechas entre fuentes, y revisión de consistencia de códigos de empresa entre archivos.

---

## 📚 Referencias (formato IEEE)

[1] Kaggle, "JPX Tokyo Stock Exchange Prediction," *Kaggle Competitions*, 2022. [Online]. Available: https://www.kaggle.com/competitions/jpx-tokyo-stock-exchange-prediction/overview. [Accessed: Aug. 31, 2026].

[2] Kaggle, "JPX Tokyo Stock Exchange Prediction — Data," *Kaggle Competitions*, 2022. [Online]. Available: https://www.kaggle.com/competitions/jpx-tokyo-stock-exchange-prediction/data. [Accessed: Aug. 31, 2026].

[3] IBM, "What is Big Data?," *IBM Think*, 2026. [Online]. Available: https://www.ibm.com/think/topics/big-data. [Accessed: Aug. 31, 2026].

[4] Japan Exchange Group, "Overview of TDnet," *JPX Official Website*, 2022. [Online]. Available: https://www.jpx.co.jp/english/equities/listing/disclosure/tdnet/index.html. [Accessed: Aug. 31, 2026].

[5] QUICK Corp., "QUICK APIs — Data Coverage (Nikkei/NQN News)," *QUICK Corporate Website*, 2022. [Online]. Available: https://corporate.quick.co.jp/en/apis/. [Accessed: Aug. 31, 2026].

---

## 📁 Archivos de este repositorio

```
02-week/
├── README.md                          ← este archivo (resumen técnico)
├── OPCIONAL ACTIVITY 02.pdf   ← documento completo
└── Fuentes_datos_Semana2.xlsx          ← anexo con inventario y V's del Big Data
```

---

## 👥 Integrantes

| Nombre | Rol |
|---|---|
| **Zara Melisa Monroy Vera** | Desarrolladora |
| **Iván David Cardozo Charry** | Desarrollador |

---

## 🎓 Información Académica

**Programa:** Ingeniería Industrial
**Asignatura:** Electiva VI Ciencia de Datos (Cód. 69109) [Pénsum 40D, Grupo 1]
**Institución:** Corporación Universitaria del Huila — CORHUILA
**Periodo:** 2026-B

---

> Actividad formativa desarrollada para la Unidad 1 · Fundamentos de Ciencia de Datos y Big Data — Semana 2, Corte 1.
