# Diseño de una Arquitectura de Datos: Mercado Bursátil de Tokio (JPX)

**Semana 3 — Ciencia de Datos | Corte 1 | Actividad formativa (opcional, sin nota)**

![Kaggle](https://img.shields.io/badge/Kaggle-JPX_Dataset-20BEFF?style=flat-square&logo=kaggle)
![Architecture](https://img.shields.io/badge/Arquitectura-Data_Lake_%2F_Batch-blue?style=flat-square)
![Data](https://img.shields.io/badge/Entrega-GitHub-black?style=flat-square&logo=github)
![IEEE](https://img.shields.io/badge/Referencias-Formato_IEEE-orange?style=flat-square)

---

## 📌 Descripción

Tercera etapa del proyecto de ciencia de datos aplicado al mercado bursátil de Tokio. Este documento diseña la **arquitectura de datos** completa —fuentes → ingesta → almacenamiento → procesamiento → análisis/BI—, justifica la elección entre data lake/warehouse y batch/streaming, y propone una herramienta candidata para cada etapa del flujo.

> 📄 El desarrollo completo (portada, abstract, marco teórico) está en `OPCIONAL ACTIVITY 03.pdf`, incluido en esta carpeta.

---

## 🎯 Objetivos

- **Dibujar** el flujo completo de la arquitectura de datos: fuentes → ingesta → almacenamiento → procesamiento → análisis/BI.
- **Justificar** la elección entre data lake y data warehouse, y entre procesamiento batch y streaming.
- **Nombrar** una herramienta candidata para cada etapa (ingesta, procesamiento, BI) y justificar su elección.

---

## 🏗️ Arquitectura del flujo

![Arquitectura de datos JPX](images/arquitectura_datos_semana3.png)
*Figura 1. Arquitectura de datos propuesta para la predicción de retornos en el mercado JPX. Elaboración propia, asistida con IA (Claude, Anthropic).*

---

## ⚖️ Decisiones de arquitectura justificadas

| Decisión | Elección | Justificación |
|---|---|---|
| Data lake vs. data warehouse | **Data Lake** | Las fuentes combinan tres niveles de estructura (estructurado, semiestructurado, no estructurado); un warehouse exigiría transformación previa innecesaria |
| Batch vs. streaming | **Batch** | Las fuentes se actualizan diaria/semanalmente, no en tiempo real; el problema de negocio no exige respuesta inmediata |

---

## 🛠️ Herramientas candidatas por etapa

| Etapa | Herramienta candidata | Justificación |
|---|---|---|
| **Ingesta** | Apache Airflow | Orquesta cargas batch diarias/semanales desde múltiples fuentes, gestionando dependencias entre tareas |
| **Procesamiento** | Python (Pandas / PySpark) | Pandas para el volumen actual; PySpark si el volumen de noticias/comunicados creciera |
| **BI / Visualización** | Power BI | Dashboards interactivos de ranking de retornos y comparación sectorial |

📎 Tablas completas en `Arquitectura_datos_Semana3.xlsx`.

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
03-week/
├── README.md                       ← este archivo (resumen técnico)
├── OPCIONAL ACTIVITY 03.pdf   ← documento completo
├── Arquitectura_datos_Semana3.xlsx  ← anexo con decisiones y herramientas por etapa
└── imagenes/
    └── arquitectura_datos_semana3.png
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

> Actividad formativa desarrollada para la Unidad 1 · Fundamentos de Ciencia de Datos y Big Data — Semana 3, Corte 1.
