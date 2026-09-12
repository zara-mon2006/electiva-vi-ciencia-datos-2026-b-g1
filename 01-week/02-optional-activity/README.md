# Encuadre de un Proyecto de Datos: Predicción de Retornos en el Mercado Bursátil de Tokio (JPX)

**Semana 1 — Ciencia de Datos | Corte 1 | Actividad formativa (opcional, sin nota)**

![Kaggle](https://img.shields.io/badge/Kaggle-JPX_Dataset-20BEFF?style=flat-square&logo=kaggle)
![Analytics](https://img.shields.io/badge/Analítica-Predictiva-blue?style=flat-square)
![Data](https://img.shields.io/badge/Entrega-GitHub-black?style=flat-square&logo=github)
![IEEE](https://img.shields.io/badge/Referencias-Formato_IEEE-orange?style=flat-square)

---

## 📌 Descripción

Primera etapa de un proyecto de ciencia de datos aplicado a un caso real: la construcción de portafolios de inversión en el mercado bursátil japonés. Este documento **encuadra el proyecto**, formulando la pregunta de negocio, identificando los datos y fuentes necesarias, describiendo la decisión que el resultado habilitaría, y clasificando el tipo de analítica requerido. El trabajo se desarrolla sobre el dataset **JPX Tokyo Stock Exchange Prediction**, publicado en Kaggle por Japan Exchange Group (JPX).

> 📄 El desarrollo completo (portada, abstract, marco teórico) está en `OPCIONAL ACTIVITY 01.pdf`, incluido en esta carpeta.

---

## 🎯 Objetivos

- **Formular** una pregunta de negocio clara y accionable sobre la toma de decisiones de inversión en el mercado bursátil japonés.
- **Identificar** los datos necesarios para responder dicha pregunta y las fuentes de las cuales pueden obtenerse.
- **Describir** la decisión o acción concreta de negocio que el resultado del análisis permitiría tomar.
- **Clasificar** el tipo de analítica de datos requerido para resolver la pregunta de negocio planteada.

---

## 🧩 Encuadre del proyecto

| Componente | Contenido |
|---|---|
| **Pregunta de negocio** | ¿Es posible predecir el retorno futuro de cada acción del mercado bursátil japonés, con el fin de generar un ranking que maximice la diferencia de retorno entre las 200 acciones con mejor desempeño esperado y las 200 con peor desempeño esperado? |
| **Datos y fuentes** | Precios históricos (`stock_prices.csv`), resultados financieros (`financials.csv`) e identificación de empresa/industria (`stock_list.csv`), todos del dataset JPX Tokyo Stock Exchange Prediction en Kaggle |
| **Decisión esperada** | Composición de un portafolio de inversión: compra de las 200 acciones con mayor retorno esperado, venta/exclusión de las 200 con menor retorno esperado |
| **Tipo de analítica** | Predictiva (núcleo), con componente prescriptivo en la recomendación final de compra/venta |

📎 Tabla completa de datos y fuentes en `Datos_y_fuentes_Semana1.xlsx`.

---

## 📚 Referencias (formato IEEE)

[1] Kaggle, "JPX Tokyo Stock Exchange Prediction," *Kaggle Competitions*, 2022. [Online]. Available: https://www.kaggle.com/competitions/jpx-tokyo-stock-exchange-prediction/overview. [Accessed: Aug. 31, 2026].

[2] Kaggle, "JPX Tokyo Stock Exchange Prediction — Data," *Kaggle Competitions*, 2022. [Online]. Available: https://www.kaggle.com/competitions/jpx-tokyo-stock-exchange-prediction/data. [Accessed: Aug. 31, 2026].

[3] Qlik, "Embrace the Future — Make the Move from Descriptive to Prescriptive Analytics," *Qlik Blog*, 2022. [Online]. Available: https://www.qlik.com/blog/embrace-the-future-moving-from-descriptive-to-prescriptive-analytics. [Accessed: Aug. 31, 2026].

---

## 📁 Archivos de este repositorio

```
01-week/
├── README.md                          ← este archivo (resumen técnico)
├── OPCIONAL ACTIVITY 01.pdf            ← documento completo
└── Datos_y_fuentes_Semana1.xlsx        ← anexo con la tabla de datos y fuentes
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

> Actividad formativa desarrollada para la Unidad 1 · Fundamentos de Ciencia de Datos y Big Data — Semana 1, Corte 1.
