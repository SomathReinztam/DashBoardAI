"""
dashBoardAI.py

"""

import pandas as pd
import os
from typing import TypedDict, Annotated, Sequence

from langchain_experimental.tools.python.tool import PythonAstREPLTool
from langchain_groq import ChatGroq
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


from langgraph.graph import StateGraph, END, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode


df = pd.read_csv('iris.csv', sep=',')

# Le damos acceso al DataFrame df.
tools = [PythonAstREPLTool(locals={'df': df})]

# Usamos baja temperatura para el analista (precición) y mas alta para el coder (creatividad).
llm_analyst = ChatGroq(model_name="llama3-70b-8192", temperature=0).bind_tools(tools)
llm_coder = ChatGroq(model_name="llama3-70b-8192", temperature=0.4)


# DEFINICIÓN DE PROMPTS PARA LOS AGENTES

Analyst_system_template = """
Eres un experto analista de datos. Tu única herramienta es un REPL de Python para inspeccionar un DataFrame de pandas llamado 'df'.

Tu misión es realizar un análisis exhaustivo del 'df' para generar un informe completo. Sigue estos pasos de forma metódica:
1.  **Exploración Inicial:** Comienza usando herramientas como `df.info()` y `df.columns` para entender la estructura básica, los tipos de datos y los valores nulos.
2.  **Análisis Descriptivo:** Usa `df.describe()` para obtener estadísticas clave de las columnas numéricas. Para las categóricas, usa `df['columna'].value_counts()`.
3.  **Razonamiento y Planificación:** En cada paso, piensa qué información has obtenido y cuál es el siguiente paso lógico para completar tu análisis. Llama a una sola herramienta por vez.
4.  **Síntesis Final:** Cuando hayas recopilado toda la información necesaria, y solo entonces, genera un informe final completo en formato Markdown. Este informe debe incluir:
    - Un resumen de la estructura del DataFrame.
    - Un análisis descriptivo detallado.
    - Código Python para generar al menos 2 visualizaciones relevantes usando `plotly.express` (ej. histograma, gráfico de dispersión, boxplot). NO ejecutes el código de visualización, solo escríbelo en bloques de código.
No inventes datos. Basa todo tu informe en los resultados reales de las herramientas. Tu respuesta final debe ser únicamente el informe, sin ningún razonamiento previo.
"""

Analyst_human_template = """
Por favor, analiza el DataFrame 'df' y entrégame un informe detallado con el análisis y el código para las visualizaciones.
"""


Coder_system_template = """
Eres un desarrollador experto en Streamlit y un talentoso diseñador de interfaces.
Tu tarea es tomar un informe de análisis de datos de un DataFrame 'df' y convertirlo en una aplicación de Streamlit funcional, interactiva y estéticamente agradable.
El DataFrame 'df' ya está cargado como 'df = pd.read_csv('iris.csv', sep=',')'

Sigue estas directrices:
-   Usa un título claro (`st.title`) y encabezados (`st.header`, `st.subheader`) para estructurar la aplicación.
-   Muestra los datos y resúmenes en formatos limpios (ej. `st.dataframe`, `st.metric`).
-   Implementa las visualizaciones proporcionadas usando la librería `plotly.express`. Asegúrate de que el código sea correcto y se muestre con `st.plotly_chart`.
-   Organiza el contenido de forma lógica, usando `st.tabs` o `st.columns` si mejora la legibilidad.
-   El código debe ser completo, autocontenido y listo para ser guardado en un archivo `.py` y ejecutado.
-   Asegúrate de incluir todos los imports necesarios (streamlit, pandas, plotly.express).
"""

Coder_human_template = """
Aquí tienes el informe de análisis de datos. Por favor, crea el código completo para una aplicación de Streamlit basada en él.

Informe:
{report}
"""

coder_prompt = ChatPromptTemplate.from_messages([
    ("system", Coder_system_template),
    ("human", Coder_human_template)
])

# Estructuras de datos del estado del agente o multi-agente en canda momento
class State(TypedDict):
    # La secuencia de mensajes representa la conversación. add_messages la actualiza.
    messages: Annotated[Sequence[BaseMessage], add_messages]
    # El reporte de analisis de datos generado por Analyst
    report_md: str | None
    # El codigo del dashboard generado por Coder.
    dashboard_code: str | None

# definición del los nodos del grafo

def analyst_agent_node(state: State):
    """Nodo del agente analista: invoca al LLM para decidir el siguiente paso o generar el informe."""
    print("--- nodo analista ---")
    response = llm_analyst.invoke(state['messages'])
    return {"messages": [response]}

def coder_agent_node(state: State):
    """Nodo del agente Coder: genera el código del dashboard de Streamlit."""
    print("--- nodo coder ---")
    # El informe final del analista es el último mensaje.
    report = state["messages"][-1].content
    
    # Creamos una cadena para el coder
    coder_chain = coder_prompt | llm_coder | StrOutputParser()
    
    response_code = coder_chain.invoke({"report": report})
    
    return {
        "messages": [AIMessage(content="Código del dashboard generado.")],
        "dashboard_code": response_code,
        "report_md":report
    }


def should_continue(state: State):
    """Decide el siguiente paso después de que el analista haya actuado."""
    last_message = state['messages'][-1]
    # Si el LLM generó una llamada a herramienta, la ejecutamos.
    if last_message.tool_calls:
        return "tools"
    # Si no hay llamadas a herramientas, significa que el analista ha terminado y ha generado el informe.
    # El siguiente paso es el Coder.
    return "coder"



tool_node = ToolNode(tools)

builder = StateGraph(State)

builder.add_node("Analyst", analyst_agent_node)
builder.add_node("tools", tool_node)
builder.add_node("Coder", coder_agent_node)

builder.add_edge(START, "Analyst")
builder.add_edge("tools", "Analyst")
builder.add_edge("Coder", END)

builder.add_conditional_edges(
    "Analyst",
    should_continue,
    {
        "tools": "tools",  # Si nececita herramientas, va al nodo de herramientas
        "coder": "Coder"    # Si ha terminado, va al nodo Coder
    }
)

print("\n")

# Construimos el multi-agente
graph = builder.compile()

# Exportamos una gráfica del grafo, nos da una impresión de cual es la 
# arquitectura del agente y por tanto una idea de como funciona.
image_data = graph.get_graph().draw_mermaid_png()
with open("grafo_del_agente.png", "wb") as image_file:
    image_file.write(image_data)
print("Imagen guardada como grafo_del_agente.png")



initial_state = {
    "messages": [
        SystemMessage(content=Analyst_system_template),
        HumanMessage(content=Analyst_human_template)
    ]
}

final_state = None
print("\n--- INICIANDO EJECUCION DEL GRAFO ---")
for event in graph.stream(initial_state, stream_mode="values"):
    print("\n--- ESTADO PARCIAL DEL GRAFO ---")
    # Se imprime el estado en cada paso para depuracion
    print(event)
    final_state = event

print("\n" + "="*50)
print("--- EJECUCION DEL GRAFO FINALIZADA ---")
print("="*50 + "\n")



if final_state and final_state.get("report_md"):
    dashboard_code = final_state["report_md"]
    
    print("--- CÓDIGO DEL REPORT GENERADO ---")
    print(dashboard_code)

    file_name = "report_generado.md"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(dashboard_code)
    
    print("\n" + "-"*50)
    print(f"✅ El código del reporte se ha guardado en '{file_name}'")
    print(f"Para ejecutarlo, usa el comando: streamlit run {file_name}")
    print("-"*50)
else:
    print("❌ No se pudo generar el código del reporte.")
    print("Estado final:", final_state)

print("\n")


if final_state and final_state.get("dashboard_code"):
    dashboard_code = final_state["dashboard_code"]
    
    print("--- CÓDIGO DEL DASHBOARD GENERADO ---")
    print(dashboard_code)

    file_name = "dashboard_generado.md"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(dashboard_code)
    
    print("\n" + "-"*50)
    print(f"✅ El código del dashboard se ha guardado en '{file_name}'")
    print(f"Para ejecutarlo, usa el comando: streamlit run {file_name}")
    print("-"*50)
else:
    print("❌ No se pudo generar el código del dashboard.")
    print("Estado final:", final_state)


