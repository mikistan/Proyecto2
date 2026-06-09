# Título del Proyecto: Análisis inicial y selección de problema

## Descripción:
Este proyecto se enfoca en realizar un Análisis Exploratorio de Datos (EDA) sobre diversos conjuntos de datos para identificar una problemática de Machine Learning. El objetivo es diagnosticar las características de los datos, entender su relevancia y seleccionar un problema específico (regresión, clasificación, clustering o predicción) que sea desafiante y con impacto real.

## Conjuntos de datos analizados:
1. **Facebook Live Sellers (Live_20210128.csv):** Datos de interacción en publicaciones de Facebook Live en Tailandia, incluyendo reacciones, comentarios y compartidos. Se analizaron patrones de interacción y popularidad.
2. **Wine Quality (winequality-white.csv):** Propiedades fisicoquímicas de vinos blancos y su calidad percibida. Se exploró la relación entre componentes químicos y la calificación de calidad.
3. **CO2 Emissions (co2.csv):** Características de vehículos y sus emisiones de CO2. Se investigó cómo el tamaño del motor, cilindros y consumo de combustible influyen en las emisiones.
4. **Individual Household Electric Power Consumption (household_power_consumption.txt):** Registros de consumo eléctrico doméstico a nivel de minuto durante varios años. Análisis de patrones temporales de consumo y sus componentes.

## Resumen del EDA inicial:
* **Live_20210128.csv (Facebook Live Sellers):** Distribuciones asimétricas en reacciones, alta correlación entre tipos de reacciones. Ausencia de nulos tras limpieza. Los outliers representan interacciones excepcionalmente altas, no errores.
* **winequality-white.csv (Wine Quality):** Calidad concentrada en valores medios (5-7). Duplicados eliminados. Correlación de alcohol y densidad con la calidad. Outliers presentes en casi todas las propiedades químicas, reflejando diversidad.
* **co2.csv (CO2 Emissions):** Distribuciones sesgadas a la derecha en tamaño de motor, cilindros y consumo. Altas correlaciones entre consumo, tamaño del motor, cilindros y emisiones de CO2. Outliers son comunes debido a la variedad de vehículos.
* **household_power_consumption.txt (Consumo Energía):** Series de tiempo con datos a nivel de minuto. Valores nulos imputados con interpolación temporal. Distribuciones del consumo activo e intensidad concentradas en valores bajos con picos. El voltaje es estable. Fuertes correlaciones entre las variables de consumo.

## Problema seleccionado: regresión para la predicción del consumo de energía doméstica

**Descripción detallada:** El problema elegido es predecir el Global_active_power en el dataset de consumo de energía doméstica (household_power_consumption.txt) usando un modelo de regresión. Esto implica desarrollar un modelo capaz de estimar el consumo eléctrico futuro basándose en las características históricas del consumo y atributos temporales.

**Justificación de la elección:**
* La predicción del consumo energético es crucial para la gestión eficiente de recursos, optimización de costos y detección de anomalías.
* El dataset a nivel de minuto presenta una rica estructura temporal, lo que me permite explorar y aplicar técnicas avanzadas de modelado de series de tiempo. Esto añade complejidad y valor al proyecto.
* La disponibilidad de múltiples métricas de consumo y la posibilidad de generar características temporales (hora, día de la semana, mes, año) brindan una excelente oportunidad para la ingeniería de características y un análisis profundo.
* Permite explorar la volatilidad y estacionalidad del consumo, un problema fundamental en la ciencia de datos y la ingeniería.

**Objetivos específicos:**
1. Preprocesar el dataset, incluyendo la creación de nuevas características temporales (hour, day_of_week, day_of_month, month, year).
2. Desarrollar un modelo de regresión que prediga el Global_active_power con la mayor precisión posible.
3. Evaluar el rendimiento del modelo utilizando métricas adecuadas para problemas de regresión en series temporales.
4. Identificar los factores más influyentes en el consumo de energía.

## Instrucciones para ejecutar:

Sigue estos pasos para configurar el entorno y ejecutar los análisis del proyecto:

### 1. Prerrequisitos
Asegúrate de tener instalado Python (versión 3.12 o superior) y un gestor de paquetes como `pip`.

### 2. Clonar el repositorio
Clona este proyecto en tu máquina local y accede a la carpeta raíz:

git clone https://github.com/mikistan/Proyecto2.git

cd Proyecto2

### 3. Instalar las librerías necesarias
El script de funciones en la carpeta /utilidades y los notebooks de análisis dependen de varias librerías de ciencia de datos. Instálalas ejecutando el siguiente comando en tu terminal:

pip install numpy pandas matplotlib seaborn jupyterlab

### 4. Ejecución del proyecto
Nota sobre las funciones: Los notebooks (.ipynb) importan funciones analíticas centralizadas desde la carpeta /utilidades. Asegúrese de iniciar Jupyter desde la raíz del proyecto para evitar errores con las rutas relativas.

Para abrir y explorar los cuadernos de trabajo, inicia Jupyter Lab o ábralo desde visual studio code:

jupyter lab

Flujo de ejecución sugerido:

* Fase de Exploración (/EDA): Ejecuta los notebooks individuales (EDA_dataset1.ipynb, etc.) para comprender el comportamiento y la limpieza de cada fuente de datos.

* Fase Final (/selected_dataset): Revisa el dataset definitivo en selected_dataset.csv y ejecuta EDA_selected_dataset.ipynb para ver las conclusiones y resultados finales del proyecto.

## Autores:
*   **Miguel Méndez:** Paupérrimo estudiante del Gran Teacher Jesus.

## Licencia:
Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.