# DashBoardAI 🧠📊 Agente Multi-Rol para Análisis y Visualización de Datos
## Por Thomas Martínes Velásques - Estudiante de Matemáticas - Universidad Nacional 

**Proyecto creado para la Hackatón Deeppunk 2025**

---

### 🚀 ¿Qué es DashBoardAI?

DashBoardAI es un sistema multi-agente que automatiza el proceso de análisis y visualización de datos. A partir de un simple archivo CSV, el sistema puede generar de forma autónoma:

1.  Un **informe estadístico detallado** en formato Markdown.
2.  Un Markdown que contiene una **aplicación web interactiva (dashboard)** construida con Streamlit.
3.  Se supone que los datos ya estan limpios. El agente solo se límita al análisis.

Este proyecto utiliza el poder de los Grandes Modelos de Lenguaje (LLMs) y arquitecturas de agentes, como **LangGraph** y **LangChain**, para orquestar un flujo de trabajo cognitivo donde diferentes agentes especializados colaboran para transformar datos crudos en insights accionables y visualizaciones funcionales.

### ✨ Características Principales

-   🤖 **Arquitectura Multi-Agente:** Un agente *Analista* interpreta los datos y un agente *Coder* escribe el código del dashboard, simulando un equipo de ciencia de datos.
-   🛠️ **Agentes con Herramientas:** Los agentes no solo razonan, sino que ejecutan código Python (`PythonAstREPLTool`) para realizar análisis reales sobre el DataFrame.
-   🔄 **Flujo de Trabajo Autónomo:** El sistema gestiona el ciclo completo: desde la ingesta de datos y el análisis hasta la generación de un producto final archivo Markdown que contiene el ejecutable (el dashboard).
-   💻 **Generación de Código Funcional:** El resultado final no es solo un informe estático, sino un archivo marckdown que contiene aplicación Streamlit lista para ser desplegada.

---

### 🔧 Flujo de Trabajo y Arquitectura

El proceso se modela como un grafo de estados donde cada nodo representa un agente o una herramienta.

![Grafo del Agente](https://github.com/SomathReinztam/DashBoardAI/raw/main/DashBoardAI/grafo_del_agente.png)

1.  **Carga de Datos:** El usuario carga un archivo CSV a traves de un DataFrame de pandas.
2.  **Agente Analista (`Analyst`):**
    -   Recibe el DataFrame.
    -   Utiliza la herramienta `PythonAstREPLTool` para ejecutar código de análisis (e.g., `df.describe()`, `df.corr()`, etc.).
    -   Genera un informe detallado en Markdown (`report_generado.md`) con sus hallazgos y sugerencias de visualización.
3.  **Agente Programador (`Coder`):**
    -   Recibe el informe del analista.
    -   Escribe el código Python para una aplicación Streamlit que visualiza los insights del informe usando librerías como Plotly.
    -   Guarda el código en un archivo `dashboard_generado.mk`, que contiene el código para generar el dashboard en Streamlit.

---

### 📚 Tecnologías Utilizadas

-   **Orquestación de Agentes:** LangGraph y LangChain
-   **Modelo de Lenguaje (LLM):** LLaMA3-70B a través de la API de Groq para inferencia de alta velocidad. Donde resalto que LLama es un LLM de código abierto.
-   **Dashboard Interactivo:** Streamlit
-   **Visualización de Datos:** Plotly
-   **Análisis de Datos:** Pandas

---

### ▶️ Instalación y Uso

Sigue estos pasos para poner en marcha el proyecto en tu entorno local.

#### Prerrequisitos

-   Python 3.10 o superior (desarrollado y probado con Python 3.11).
-   Git para clonar el repositorio.

#### 1. Clonar el Repositorio

```bash
git clone https://github.com/SomathReinztam/DashBoardAI.git
cd DashBoardAI
```

#### 2. Crear un Entorno Virtual (Recomendado)

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

#### 3. Instalar Dependencias

Todas las librerías necesarias se encuentran en `requirements.txt`.

```bash
pip install -r requirements.txt
```

#### 4. Configurar la API Key

Este proyecto requiere una clave de API de **Groq**. Puedes obtener una de forma gratuita en [su plataforma](https://console.groq.com/keys).

Crea un archivo llamado `.env` en la raíz del proyecto y añade tu clave:

```
# .env
GROQ_API_KEY="tu_api_key_aqui"
```

El programa cargará esta variable de entorno automáticamente.

#### 5. Ejecutar el Agente

Asegúrate de tener tu archivo de datos (por ejemplo, `mi_dataset.csv`) en el directorio del proyecto. Luego, ejecuta el script principal:

```bash
# Reemplaza 'ruta/a/tu/dataset.csv' con la ubicación de tu archivo
python main.py --file 'ruta/a/tu/dataset.csv'
```

#### 6. Revisar los Resultados

Una vez que el script finalice, encontrarás dos archivos nuevos:

-   `report_generado.md`: El informe de análisis estadístico.
-   `dashboard_generado.py`: El script de la aplicación Streamlit.

#### 7. Lanzar el Dashboard

Para ver tu dashboard interactivo, ejecuta el siguiente comando en tu terminal:

```bash
streamlit run dashboard_generado.py
```

---

### 📂 Estructura de Entrada y Salida

-   **Entrada:** Cualquier archivo CSV que pueda ser leído por `pandas.read_csv()`.
-   **Salida:**
    -   `report_generado.md`: Un archivo Markdown con el informe de análisis.
    -   `dashboard_generado.py`: Un script de Python listo para ser ejecutado con Streamlit.

---

### ⚠️ Advertencia de Seguridad Importante

Este proyecto utiliza la herramienta `PythonAstREPLTool`, que otorga al agente la capacidad de **ejecutar código Python arbitrario** en el sistema donde se corre. Esto representa una vulnerabilidad de seguridad significativa.


**No ejecutes este agente en un entorno de producción o con datos sensibles sin implementar medidas de sandboxing adecuadas.** Úsalo con fines educativos y de experimentación en un entorno controlado.

### ⚠️ Nota

Si quieres que el agente analice un data frame diferente al proporcionado en este repositorio debes especificar el cambio dentro de la bariable Coder_system_template en el archivo dashBoardAI.py, cambiando el nombre de la referencia del data frame del anterior `df = pd.read_csv(iris.csv, sep=',')` a el nuevo.

---

### ⚖️ Consideraciones Éticas

-   **Transparencia:** Los LLMs pueden cometer errores o "alucinar". Revisa siempre el informe y el código generado antes de tomar decisiones basadas en ellos.
-   **Privacidad de Datos:** No utilices este sistema con datos personales o sensibles sin haber aplicado previamente técnicas de anonimización.
-   **Uso Responsable:** Esta herramienta está diseñada para aumentar y complementar el juicio humano, no para reemplazarlo. La supervisión de un experto es fundamental.

---

### 🌍 Impacto y Visión

-   **Democratización del Análisis:** Permite a usuarios sin experiencia en programación obtener análisis y dashboards interactivos de forma rápida.
-   **Aceleración del Prototipado:** Reduce drásticamente el tiempo necesario para la exploración inicial de nuevos conjuntos de datos.
-   **Sistemas Auto-Explicativos:** El informe generado sirve como documentación del "razonamiento" del LLM, abriendo la puerta a sistemas de IA más transparentes.
-  **Divulgación de como se desarrollan los agentes** En internet, creo que no hay mucho contenido en español del como se desarrollan los agentes a traves del framework de **langGraph** y **langChain**, este trabajo sirve como un muy buen ejemplo para empezar a estudiar el desarrollo de agentes dado que la arquitectura desarrollada aquí es simple.

---

### ✨ Cosas a mejorar

- La arquitectura del sistema multi-agente es bastante sencilla, principalmente debido a las limitaciones de utilizar una API gratuita, lo cual restringe las opciones de diseño e implementación.

- En futuras versiones del proyecto, se podrá mejorar la abstracción y robustez del sistema. Actualmente, cambiar el DataFrame a analizar requiere modificaciones manuales poco prácticas. Además, se podría trabajar para que el resultado final sea un ejecutable autónomo del dashboard en Python, en lugar de un archivo Markdown que lo contiene.

- También debido a las restricciones de la API gratuita, fue necesario limitar la cantidad de DataFrames que pueden analizarse en paralelo. Esta es una limitación significativa, ya que en contextos reales los datasets suelen estar relacionados y deben ser analizados de forma conjunta.

- El agente no hace limpiesa de datos o pre-procesamiento de los datos. En futuras versiones esta caracteristica se podría implementar
