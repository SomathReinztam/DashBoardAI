
# 🧠📊 Agente Multi-Rol para Análisis de Datos y Visualización con LangGraph + Streamlit

Este proyecto implementa un **multi-agente inteligente** construido con [LangGraph](https://github.com/langchain-ai/langgraph) y [LangChain](https://www.langchain.com/) que realiza de manera autónoma un **análisis estadístico de un DataFrame de pandas** y genera un **dashboard interactivo con Streamlit** a partir del análisis.

## 🚀 ¿Qué hace este proyecto?

Este sistema simula la colaboración entre dos expertos virtuales:
- 👨‍🔬 **Analyst Agent**: un analista de datos que explora, describe y sintetiza estadísticamente un DataFrame.
- 👨‍💻 **Coder Agent**: un desarrollador que convierte el informe del analista en una aplicación visual y ejecutable en Streamlit.

### Flujo de trabajo automatizado:
1. El analista inspecciona el DataFrame (`df`) usando herramientas de Python como `df.info()`, `df.describe()` y llamadas a visualizaciones (sin ejecutarlas).
2. El resultado es un informe detallado en formato Markdown que incluye resúmenes y código para visualizaciones con Plotly.
3. El programador toma ese informe y genera una app de Streamlit limpia, funcional e interactiva.

## 🔧 Detalles técnicos

### 📚 Tecnologías principales
- **LangGraph + LangChain**: para modelar y coordinar agentes con memoria y herramientas.
- **ChatGroq (LLaMA3-70B)**: LLMs especializados en razonamiento estructurado y generación creativa.
- **PythonAstREPLTool**: permite a los LLM ejecutar código sobre el DataFrame en un entorno controlado.
- **Streamlit**: framework para visualización rápida de datos y dashboards interactivos.
- **Plotly**: visualizaciones interactivas para la web.

### 🧩 Estructura del sistema
- `Analyst Agent`: accede a `df`, genera preguntas, ejecuta código Python real para explorar datos y sintetiza un informe.
- `ToolNode`: ejecuta las herramientas necesarias cuando el analista decide usarlas.
- `Coder Agent`: interpreta el informe y crea código listo para ejecutar con `streamlit run`.

### 📂 Entrada y salida
- **Entrada**: cualquier archivo CSV legible por pandas (`df = pd.read_csv()`).
- **Salida**:
  - Un archivo de texto con el informe de análisis (`report_generado.txt`).
  - Un archivo `.py` con el dashboard listo para correr (`dashboard_generado.py`).

## 🧠 ¿Por qué es innovador?

- 🤖 **Multi-agencia cognitiva real**: usa una arquitectura de flujo condicional entre agentes especializados.
- 🛠️ **Agentes con herramientas ejecutables**: no solo "hablan", también actúan sobre datos reales.
- 🔄 **Autonomía en ciclos de razonamiento**: el analista decide cuándo necesita más datos y cuándo pasar al programador.
- 💻 **Producción de código funcional**: el resultado no es un informe estático, sino una aplicación real que se puede desplegar.

## 🌍 Impacto del proyecto

- Democratiza el análisis de datos: permite a usuarios sin conocimientos avanzados obtener insights y dashboards interactivos automáticamente.
- Acelera el prototipado en ciencia de datos: ideal para exploración rápida de nuevos datasets.
- Abre puertas a sistemas auto-explicativos: los LLM no solo dan respuestas, también documentan su pensamiento.

## ⚖️ Consideraciones éticas

- ⚠️ **Transparencia de decisiones**: el informe debe revisarse antes de tomar decisiones críticas, ya que el LLM puede cometer errores.
- 🔒 **Privacidad de datos**: asegúrate de no usar este sistema con datos sensibles sin aplicar técnicas de anonimización o controles adecuados.
- 🤖 **Uso responsable de la automatización**: este agente **no reemplaza** el juicio humano experto, sino que lo complementa.

## ▶️ ¿Cómo usarlo?

1. Instala dependencias necesarias:
   ```bash
   pip install pandas streamlit plotly langgraph langchain langchain-groq
   ```

2. Configura tu archivo `.env` con tu clave de Groq:
   ```env
   GROQ_API_KEY=tu_clave
   ```

3. Ejecuta el script principal:
   ```bash
   python main.py
   ```

4. Corre el dashboard generado:
   ```bash
   streamlit run dashboard_generado.py
   ```

## 📌 Autor

Desarrollado por Thomas Martínez Velásquez  
Estudiante de Matemáticas – Universidad Nacional de Colombia
