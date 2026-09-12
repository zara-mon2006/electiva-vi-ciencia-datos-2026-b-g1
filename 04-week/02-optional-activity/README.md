# Tipos de Analítica y Consideraciones Éticas: Predicción de Retornos en el Mercado Bursátil de Tokio (JPX)

**Semana 4 — Ciencia de Datos | Corte 1 | Actividad formativa (opcional, sin nota)**

![Kaggle](https://img.shields.io/badge/Kaggle-JPX_Dataset-20BEFF?style=flat-square&logo=kaggle)
![Analytics](https://img.shields.io/badge/Analítica-4_Tipos-blue?style=flat-square)
![Ethics](https://img.shields.io/badge/Ética-Sesgo_%2F_Mitigación-red?style=flat-square)
![IEEE](https://img.shields.io/badge/Referencias-Formato_IEEE-orange?style=flat-square)

---

## 📌 Descripción

Cuarta etapa del proyecto de ciencia de datos aplicado al mercado bursátil de Tokio. Este documento formula **cuatro preguntas**, una por cada tipo de analítica (descriptiva, diagnóstica, predictiva, prescriptiva), justifica el uso de aprendizaje automático supervisado, e identifica un riesgo ético concreto junto con su estrategia de mitigación.

> 📄 El desarrollo completo (portada, abstract, marco teórico) está en `OPCIONAL ACTIVITY 04.pdf`, incluido en esta carpeta.

---

## 🎯 Objetivos

- **Escribir** cuatro preguntas sobre el caso de estudio, una por cada tipo de analítica.
- **Indicar**, para los componentes predictivo y prescriptivo, si se usaría ML supervisado o no supervisado, y justificar por qué.
- **Describir** un posible sesgo o riesgo ético del proyecto y proponer una estrategia para mitigarlo.

---

## 🧩 Las 4 preguntas por tipo de analítica

| Tipo | Pregunta |
|---|---|
| Descriptiva | ¿Cuál fue el retorno promedio de las acciones del sector tecnológico japonés durante el último trimestre? |
| Diagnóstica | ¿Por qué ciertas acciones tuvieron retornos negativos, según sus resultados financieros trimestrales? |
| **Predictiva** | ¿Cuál será el retorno futuro de cada acción del mercado japonés en el próximo periodo de negociación? |
| **Prescriptiva** | ¿Qué acciones se deberían incluir en el segmento de compra (top 200) y cuáles en el de venta (bottom 200)? |

📎 Tabla completa en `Analitica_etica_Semana4.xlsx`.

---

## 🧠 Tipo de aprendizaje automático

**Supervisado**, dado que el dataset ya contiene una variable objetivo etiquetada (columna *target* = retorno realizado en `stock_prices.csv`), lo que permite entrenar y validar el modelo. El componente prescriptivo se deriva directamente de las predicciones del modelo supervisado.

---

## ⚠️ Riesgo ético y mitigación

**Riesgo:** sesgo hacia empresas con mayor disponibilidad de datos históricos — el modelo puede generar predicciones menos confiables para empresas pequeñas o de reciente listado, no por menor potencial de retorno real sino por menor cantidad de datos disponibles.

**Mitigación:**
1. Segmentar la evaluación del modelo por tamaño de empresa, reportando métricas separadas por segmento.
2. Establecer un umbral mínimo de calidad de datos, comunicando qué acciones quedan fuera del alcance confiable del modelo.

---

## 📚 Referencias (formato IEEE)

[1] Kaggle, "JPX Tokyo Stock Exchange Prediction," *Kaggle Competitions*, 2022. [Online]. Available: https://www.kaggle.com/competitions/jpx-tokyo-stock-exchange-prediction/overview. [Accessed: Aug. 31, 2026].

[2] Kaggle, "JPX Tokyo Stock Exchange Prediction — Data," *Kaggle Competitions*, 2022. [Online]. Available: https://www.kaggle.com/competitions/jpx-tokyo-stock-exchange-prediction/data. [Accessed: Aug. 31, 2026].

[3] IBM, "What is Big Data?," *IBM Think*, 2026. [Online]. Available: https://www.ibm.com/think/topics/big-data. [Accessed: Aug. 31, 2026].

[4] Qlik, "Embrace the Future — Make the Move from Descriptive to Prescriptive Analytics," *Qlik Blog*, 2022. [Online]. Available: https://www.qlik.com/blog/embrace-the-future-moving-from-descriptive-to-prescriptive-analytics. [Accessed: Aug. 31, 2026].

---

## 📁 Archivos de este repositorio

```
04-week/
├── README.md                       ← este archivo (resumen técnico)
├── OPCIONAL ACTIVITY 04.pdf        ← documento completo
└── Analitica_etica_Semana4.xlsx    ← anexo con preguntas, ML y riesgo ético
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

> Actividad formativa desarrollada para la Unidad 1 · Fundamentos de Ciencia de Datos y Big Data — Semana 4, Corte 1.
