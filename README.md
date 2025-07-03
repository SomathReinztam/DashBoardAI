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

También puedes optar por otras APIs como la de OpenAI o Google pero debes instalar los modulos adecuados de LangChain.

#### 5. Ejecutar el Agente

Asegúrate de tener tu archivo de datos (por ejemplo, en mi caso para este proyecto utilicé `iris.csv`) en el directorio del proyecto. Luego, ejecuta el script principal dashBoardAI.py:

```bash
dashBoardAI.py
```

#### 6. Revisar los Resultados

Una vez que el script finalice, encontrarás dos archivos nuevos:

-   `report_generado.md`: El informe de análisis estadístico.
-   `dashboard_generado.md`: El archivo Markdown que contiene el script de la aplicación Streamlit.

#### 7. Lanzar el Dashboard

Para ver tu dashboard interactivo, del archivo `dashboard_generado.md` extrae el ejecutable y copialo a un script de Python. En mi caso yo lo copié a un script llamado `streamlit.py`. Luego ejecuta el siguiente comando en tu terminal:

```bash
streamlit run streamlit.py
```

---

### 📂 Estructura de Entrada y Salida

-   **Entrada:** Cualquier archivo CSV que pueda ser leído por `pandas.read_csv()`.
-   **Salida:**
    -   `report_generado.md`: Un archivo Markdown con el informe de análisis.
    -   `dashboard_generado.md`: Un archivo Markdown que contiene un script de Python que puede ser extraido y luego ser ejecutado con Streamlit.

---

### ⚠️ Advertencia de Seguridad Importante

Este proyecto utiliza la herramienta `PythonAstREPLTool`, que otorga al agente la capacidad de **ejecutar código Python arbitrario** en el sistema donde se corre. Esto representa una vulnerabilidad de seguridad significativa.


**No ejecutes este agente en un entorno de producción o con datos sensibles sin implementar medidas de sandboxing adecuadas.** Úsalo con fines educativos y de experimentación en un entorno controlado.

---
### 🛠️ Nota

Si deseas que el agente analice un DataFrame diferente al proporcionado en este repositorio, debes modificar la variable `Coder_system_template` en el archivo `dashBoardAI.py`, cambiando la línea donde se referencia el DataFrame actual, por ejemplo:

```python
Coder_system_template = """ ... df = pd.read_csv("iris.csv", sep=",") ... """
```

Debes reemplazar `"iris.csv"` con el nombre del nuevo archivo que deseas utilizar.
Alternativamente, puedes dejar esa línea como está y simplemente asegurarte de que, en el archivo Markdown que contiene el ejecutable del dashboard de Streamlit, se haga referencia correctamente al nuevo DataFrame.

---

### ⚖️ Consideraciones Éticas

-   **Transparencia:** Los LLMs pueden cometer errores o "alucinar". Revisa siempre el informe y el código generado antes de tomar decisiones basadas en ellos.
-   **Privacidad de Datos:** No utilices este sistema con datos personales o sensibles sin haber aplicado previamente técnicas de anonimización.
-   **Uso Responsable:** Esta herramienta está diseñada para aumentar y complementar el juicio humano, no para reemplazarlo. La supervisión de un experto es fundamental.
-   **Vulnerabilidad de seguridad** Este código tiene una vulnerabilidad de seguridad importante. Se debe ser transparente con esto.

---

### 🌍 Impacto y Visión

-   **Democratización del Análisis:** Permite a usuarios sin experiencia en programación obtener análisis y dashboards interactivos de forma rápida, sin depender de software privatibo como Power BI o Tableu.
-   **Aceleración del Prototipado:** Reduce drásticamente el tiempo necesario para la exploración inicial de nuevos conjuntos de datos.
-   **Sistemas Auto-Explicativos:** El informe generado sirve como documentación del "razonamiento" del LLM, abriendo la puerta a sistemas de IA más transparentes.
-  **Divulgación de como se desarrollan los agentes** Actualmente, creo que hay poco contenido en español sobre cómo se desarrollan agentes utilizando los frameworks **LangGraph** y **LangChain**. Este trabajo puede servir como un buen punto de partida para quienes deseen iniciarse en el desarrollo de agentes, ya que presenta una arquitectura sencilla y fácil de entender.

---

### ✨ Cosas a mejorar

- La arquitectura del sistema multi-agente es bastante sencilla, principalmente debido a las limitaciones de utilizar una API gratuita, lo cual restringe las opciones de diseño e implementación.

- En futuras versiones del proyecto, se podrá mejorar la abstracción y robustez del sistema. Actualmente, cambiar el DataFrame a analizar requiere modificaciones manuales poco prácticas. Además, se podría trabajar para que el resultado final sea un ejecutable autónomo del dashboard en Python, en lugar de un archivo Markdown que lo contiene.

- También debido a las restricciones de la API gratuita, fue necesario limitar la cantidad de DataFrames que pueden analizarse en paralelo. Esta es una limitación significativa, ya que en contextos reales los datasets suelen estar relacionados y deben ser analizados de forma conjunta.

- El agente no hace limpiesa de datos o pre-procesamiento de los datos. En futuras versiones esta caracteristica se podría implementar

- En versiones futuras se podrá implementar tabien que además del análisis de los datos, el agente tambien se encargue de inferencia a aprtir de estos; construyendo modelos y hacer fine-tuning de estos de forma automática.
