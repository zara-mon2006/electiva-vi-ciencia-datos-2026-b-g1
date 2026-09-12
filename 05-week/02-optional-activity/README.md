# Dossier de Fundamentos: Consolidación del Proyecto de Predicción de Retornos en JPX 

**Semana 5 — Ciencia de Datos | Corte 1 | Actividad formativa (opcional, sin nota)**

![Kaggle](https://img.shields.io/badge/Kaggle-JPX_Dataset-20BEFF?style=flat-square&logo=kaggle)
![Dossier](https://img.shields.io/badge/Dossier-Cierre_Corte_1-purple?style=flat-square)
![Data](https://img.shields.io/badge/Entrega-GitHub-black?style=flat-square&logo=github)
![IEEE](https://img.shields.io/badge/Referencias-Formato_IEEE-orange?style=flat-square)

---

## 📌 Descripción

Dossier de cierre del Corte 1, que **consolida y mejora** los cuatro entregables previos del proyecto de predicción de retornos en el mercado bursátil de Tokio: el encuadre del proyecto (S1), la clasificación de fuentes y las V del Big Data (S2), la arquitectura de datos propuesta (S3), y los tipos de analítica junto con el riesgo ético identificado (S4). No introduce contenido nuevo, sino que articula estas cuatro piezas en una narrativa única y coherente.

> 📄 El desarrollo completo (portada, abstract, marco teórico) está en `OPCIONAL ACTIVITY 05.pdf`, incluido en esta carpeta.

---

## 🎯 Objetivos

- **Integrar** la pregunta de negocio y la decisión esperada definidas en la Semana 1.
- **Consolidar** las fuentes de datos, su clasificación y las V relevantes del Big Data (Semana 2).
- **Presentar** la arquitectura de datos propuesta (Semana 3).
- **Reunir** los tipos de analítica objetivo y el riesgo ético identificado (Semana 4).

---

## 🧩 1. Encuadre del proyecto (S1)

**Pregunta de negocio:** ¿Es posible predecir el retorno futuro de cada acción del mercado bursátil japonés, con el fin de generar un ranking que maximice la diferencia de retorno entre el top 200 y el bottom 200?

**Decisión esperada:** composición de un portafolio de inversión (compra/venta según el ranking).

## 🗂️ 2. Fuentes de datos y Big Data (S2)

| # | Fuente | Tipo |
|---|---|---|
| 1-5 | `stock_prices.csv`, `financials.csv`, `options.csv`, `trades.csv`, `stock_list.csv` | Estructurado |
| 6 | Comunicados TDnet | Semiestructurado |
| 7 | Noticias Nikkei/NQN | No estructurado |

**V's críticas:** Variedad y Veracidad.

## 🏗️ 3. Arquitectura de datos (S3)

**Flujo:** Fuentes → Ingesta batch → Data Lake → Procesamiento → Análisis/BI.
**Decisiones:** Data Lake (por variedad de estructuras) + Batch (por frecuencia diaria/semanal).

## 🧠 4. Analítica y ética (S4)

**Tipo de ML:** supervisado (variable *target* ya etiquetada).
**Riesgo ético:** sesgo hacia empresas con más datos históricos → mitigación: segmentar evaluación por tamaño de empresa.

📎 Tablas completas de las 3 secciones anteriores en `Dossier_Semana5.xlsx`.

---

## 📚 Referencias (formato IEEE)

[1] Kaggle, "JPX Tokyo Stock Exchange Prediction," *Kaggle Competitions*, 2022. [Online]. Available: https://www.kaggle.com/competitions/jpx-tokyo-stock-exchange-prediction/overview. [Accessed: Aug. 31, 2026].

[2] Kaggle, "JPX Tokyo Stock Exchange Prediction — Data," *Kaggle Competitions*, 2022. [Online]. Available: https://www.kaggle.com/competitions/jpx-tokyo-stock-exchange-prediction/data. [Accessed: Aug. 31, 2026].

[3] IBM, "What is Big Data?," *IBM Think*, 2026. [Online]. Available: https://www.ibm.com/think/topics/big-data. [Accessed: Aug. 31, 2026].

[4] Qlik, "Embrace the Future — Make the Move from Descriptive to Prescriptive Analytics," *Qlik Blog*, 2022. [Online]. Available: https://www.qlik.com/blog/embrace-the-future-moving-from-descriptive-to-prescriptive-analytics. [Accessed: Aug. 31, 2026].

[5] Japan Exchange Group, "Overview of TDnet," *JPX Official Website*, 2022. [Online]. Available: https://www.jpx.co.jp/english/equities/listing/disclosure/tdnet/index.html. [Accessed: Aug. 31, 2026].

[6] QUICK Corp., "QUICK APIs — Data Coverage (Nikkei/NQN News)," *QUICK Corporate Website*, 2022. [Online]. Available: https://corporate.quick.co.jp/en/apis/. [Accessed: Aug. 31, 2026].

---

## 📁 Archivos de este repositorio

```
05-week/
├── README.md                          ← este archivo (resumen técnico)
├── OPCIONAL ACTIVITY 05.pdf           ← documento completo
└── Dossier_Semana5.xlsx               ← anexo con tablas consolidadas de S2, S3 y S4
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

> Actividad formativa desarrollada para la Unidad 1 · Fundamentos de Ciencia de Datos y Big Data — Semana 5 (cierre Corte 1).
