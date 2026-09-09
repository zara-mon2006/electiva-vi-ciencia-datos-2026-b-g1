# Diagnóstico de Datos de un Proceso — Predicción de Tiempos de Entrega en Rappi

**Actividad · Ciencia de Datos | Caso real: Rappi**

![Rappi](https://img.shields.io/badge/Caso_real-Rappi-FF441F?style=flat-square)
![Analytics](https://img.shields.io/badge/Analítica-Descriptiva_%2F_Predictiva-blue?style=flat-square)
![Data](https://img.shields.io/badge/Datos-Estructurado_%2F_Semi_%2F_No_estructurado-green?style=flat-square)
![IEEE](https://img.shields.io/badge/Referencias-Formato_IEEE-orange?style=flat-square)

---

## 📌 Descripción

Diagnóstico de datos aplicado a un caso real de negocio: **Rappi**, la superaplicación colombiana de domicilios, y su necesidad de estimar con precisión el tiempo de entrega de cada pedido entre miles de restaurantes y usuarios. El trabajo identifica cuatro tipos de datos generados por la operación de la plataforma, clasificándolos según su nivel de estructura; formula una pregunta de analítica descriptiva y una de analítica predictiva; representa mediante un diagrama simple el flujo de la información (fuente → almacenamiento → análisis → visualización); y explica en inglés la diferencia entre ambos tipos de analítica, todo sustentado en fuentes públicas verificables sobre la operación real de la compañía.

---

## 🎯 Objetivo general

Diagnosticar los tipos de datos generados por la operación de Rappi y el tipo de analítica aplicable a su proceso de entrega, con el fin de ilustrar la clasificación de datos según su nivel de estructura y la diferencia entre analítica descriptiva y predictiva en un caso real de negocio.

## 🎯 Objetivos específicos

- **Identificar** cuatro tipos de datos generados por la operación de Rappi, clasificándolos como estructurados, semiestructurados o no estructurados.
- **Formular** una pregunta de analítica descriptiva y una pregunta de analítica predictiva relevantes para el proceso de entrega de pedidos.
- **Representar** mediante un diagrama simple el flujo de los datos desde su origen hasta su visualización (fuente → almacenamiento → análisis → visualización).
- **Explicar**, en inglés, la diferencia entre analítica descriptiva y analítica predictiva aplicada al caso de estudio.

---

## ❓ Introducción

El comercio electrónico y las plataformas de domicilios han transformado la manera en que las empresas gestionan su operación diaria, generando volúmenes considerables de información en tiempo real que deben clasificarse y analizarse adecuadamente para tomar decisiones de negocio efectivas. Un caso particularmente representativo de este fenómeno es **Rappi**, la superaplicación colombiana fundada en 2015 en Bogotá [7], que hoy opera en más de 250 ciudades de Latinoamérica [7] y ha llegado a gestionar picos de hasta 780.000 pedidos en un solo día [4].

Para que una plataforma de esta escala funcione de manera eficiente, es necesario identificar con claridad qué tipos de datos se generan en cada etapa del proceso de entrega y clasificarlos según su nivel de estructura, así como distinguir entre el tipo de analítica que describe lo que ya ocurrió y aquella que permite anticipar lo que sucederá. El presente trabajo utiliza el caso real de Rappi para ilustrar ambos conceptos, apoyándose en información pública verificable sobre cómo la compañía utiliza el análisis de datos e inteligencia artificial para calcular tiempos de preparación y optimizar rutas de entrega [1], [2].

---

## 🧠 Marco teórico

Para el desarrollo de este diagnóstico es necesario partir de dos conceptos fundamentales de la ciencia de datos. El primero es la **clasificación de los datos según su nivel de estructura**: los datos **estructurados** se organizan en un esquema fijo de filas y columnas; los datos **semiestructurados** combinan cierta organización con flexibilidad, sin un esquema rígido pero con etiquetas o metadatos; y los datos **no estructurados** carecen de un formato predefinido, como textos libres, imágenes o videos [5].

El segundo concepto es el **tipo de analítica aplicada** a un problema de negocio: la **analítica descriptiva** responde a "¿qué pasó?" mediante la agregación de datos históricos, mientras que la **analítica predictiva** responde a "¿qué pasará?" empleando modelos de aprendizaje automático entrenados sobre datos históricos [6]. Rappi ha declarado públicamente que sus equipos de datos van más allá del análisis descriptivo, logrando modelos predictivos que estiman tiempos de preparación y rutas óptimas de entrega [1], [2].

---

## 🗂️ Los 4 tipos de datos

| # | Dato | Clasificación | Referencia |
|---|---|---|---|
| 1 | Registro de cada pedido (producto, valor, hora, dirección) en la base de datos transaccional | **Estructurado** | — |
| 2 | Ubicación GPS en tiempo real de repartidores y usuarios | **Semiestructurado** | [2] |
| 3 | Calificaciones de la aplicación: 4.7 de 5 con 583 mil reseñas | **No estructurado** | [3] |
| 4 | Fotos de productos y menús de restaurantes aliados | **No estructurado** | — |

📎 Tabla completa con justificación en `Tipos_de_datos_Rappi.xlsx`.

---

## 🧩 Preguntas de analítica

**Descriptiva:** ¿Cuál fue el número total de pedidos entregados en un solo día durante el pico de demanda reportado por Rappi, equivalente a aproximadamente 780.000 pedidos gestionados en 24 horas? [4]

**Predictiva:** ¿Cuánto tiempo tomará entregar un pedido específico, considerando el tiempo de preparación en la tienda, la ubicación del repartidor disponible más cercano y las condiciones de tráfico actuales? [2]

---

## 🔄 Diagrama de flujo de datos

![Flujo de datos de Rappi](images/diagrama_flujo_rappi.png)
*Figura 1. Flujo de datos aplicado al proceso de predicción de tiempos de entrega en Rappi. Elaboración propia, asistida con IA (Claude, Anthropic), con base en [2].*

- **Fuente:** la app móvil captura el pedido, la ubicación GPS y las calificaciones.
- **Almacenamiento:** la información se consolida en las bases de datos en la nube de Rappi.
- **Análisis:** modelos de IA/ML calculan el tiempo de preparación y la mejor ruta [2].
- **Visualización:** el resultado se muestra como un mapa en tiempo real dentro de la app.

---

## 🌐 Two sentences in English

- *Descriptive analytics is defined as the process of examining historical data to summarize and explain what has already occurred within an organization; in Rappi's case, this is reflected in the company's public report of a single-day peak of approximately 780,000 orders processed across the country, a figure that could only be produced by aggregating and reviewing past transactional records after the fact [4].*

- *Predictive analytics, in contrast, is defined as the use of historical and real-time data, often through machine learning models, to forecast outcomes that have not yet happened; Rappi applies this concept directly when it calculates, before an order is even completed, the expected preparation time at a specific store and the optimal route for the nearest available courier, a data-driven approach that has been linked to a 30% increase in orders delivered in under 35 minutes [2].*

---

## ✅ Conclusión

El diagnóstico realizado sobre Rappi permitió comprobar que la clasificación de datos según su nivel de estructura y la diferenciación entre analítica descriptiva y predictiva no son conceptos abstractos, sino herramientas que una empresa colombiana real aplica activamente en su operación diaria para mejorar la eficiencia de su servicio de entregas [1], [2].

Se identificaron y clasificaron cuatro tipos de datos generados por la operación real de Rappi —registros de pedidos, ubicación GPS, calificaciones de usuarios y fotografías de productos—, evidenciando que una misma plataforma convive simultáneamente con información estructurada, semiestructurada y no estructurada, cada una con requerimientos de almacenamiento y procesamiento distintos [1], [2], [3].

Se formularon además una pregunta de analítica descriptiva y una de analítica predictiva aplicadas al mismo proceso de negocio, lo cual permitió ilustrar con claridad la diferencia funcional entre ambos tipos de analítica: mientras la primera se limita a reportar un hecho histórico ya ocurrido, la segunda anticipa un resultado futuro a partir de datos históricos y en tiempo real [2], [4].

Por otra parte, se representó mediante un diagrama simple el flujo completo de la información dentro de la plataforma, desde su captura en la aplicación móvil hasta su visualización final para el usuario, lo cual permitió comprender de forma visual cómo se articulan las distintas etapas del proceso de datos en un caso de negocio real.

Finalmente, se explicó en inglés la diferencia conceptual entre analítica descriptiva y predictiva, ejemplificando cada definición con evidencia concreta de la operación de Rappi, demostrando que ambos conceptos pueden sustentarse con datos reales y no solo con definiciones teóricas [2], [4].

---

## 📚 Referencias (formato IEEE)

[1] Portafolio, "Rappi estaría trabajando en bajar los tiempos de entrega," *Portafolio*, 2023. [Online]. Available: https://www.portafolio.co/negocios/empresas/rappi-estaria-trabajando-en-bajar-los-tiempos-de-entrega-570889. [Accessed: Aug. 31, 2026].

[2] Forbes Argentina, "Rappi cumple seis años en Argentina y lo festeja con inversiones millonarias y expansión regional," *Forbes Argentina*, 2023. [Online]. Available: https://www.forbesargentina.com/negocios/rappi-cumple-seis-anos-argentina-lo-festeja-inversiones-millonarias-expansion-regional-n48383. [Accessed: Aug. 31, 2026].

[3] Apple Inc., "Rappi - Pide Todo en Minutos," *App Store*, 2026. [Online]. Available: https://apps.apple.com/MX/app/id984044296. [Accessed: Aug. 31, 2026].

[4] Portafolio, "Este es el récord del pedido más rápido repartido por Rappi: en un día entregó 780.000 pedidos," *Portafolio*, 2025. [Online]. Available: https://www.portafolio.co/negocios/industrias/este-es-el-record-del-pedido-mas-rapido-repartido-por-rappi-en-un-dia-entrego-780-000-pedidos-488132. [Accessed: Aug. 31, 2026].

[5] IBM, "What is Big Data?," *IBM Think*, 2026. [Online]. Available: https://www.ibm.com/think/topics/big-data. [Accessed: Aug. 31, 2026].

[6] Qlik, "Embrace the Future — Make the Move from Descriptive to Prescriptive Analytics," *Qlik Blog*, 2022. [Online]. Available: https://www.qlik.com/blog/embrace-the-future-moving-from-descriptive-to-prescriptive-analytics. [Accessed: Aug. 31, 2026].

[7] La República / DPL News, "Colombia: Esta es la historia de Rappi, de regalar donas en Bogotá a conquistar la banca digital," *DPL News*, 2024. [Online]. Available: https://dplnews.com/?p=88791. [Accessed: Aug. 31, 2026].

---

## 📁 Archivos de este repositorio

05-week/parcil-c1
├── README.md                       ← este archivo (resumen técnico)
├── Tipos_de_datos_Rappi.xlsx        ← anexo con la tabla de los 4 tipos de datos
└── images/
    └── diagrama_flujo_rappi.png


> Actividad desarrollada aplicando los conceptos de clasificación de datos y tipos de analítica a un caso real de negocio: Rappi.
