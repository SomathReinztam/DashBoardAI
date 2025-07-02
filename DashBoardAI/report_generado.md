# Informe de Análisis del DataFrame 'df'

## Estructura del DataFrame

El DataFrame 'df' tiene 150 filas y 4 columnas, todas de tipo float64. Las columnas son: 'sepal length (cm)', 'sepal width (cm)', 'petal length (cm)' y 'petal width (cm)'.

## Análisis Descriptivo

El análisis descriptivo de las columnas numéricas se muestra a continuación:

* La columna 'sepal length (cm)' tiene un valor medio de 5.84 cm, con un rango de 4.3 cm a 7.9 cm.
* La columna 'sepal width (cm)' tiene un valor medio de 3.06 cm, con un rango de 2 cm a 4.4 cm.
* La columna 'petal length (cm)' tiene un valor medio de 3.76 cm, con un rango de 1 cm a 6.9 cm.
* La columna 'petal width (cm)' tiene un valor medio de 1.2 cm, con un rango de 0.1 cm a 2.5 cm.

## Visualizaciones

A continuación, se presentan dos visualizaciones relevantes para el análisis del DataFrame 'df':

### Histograma de Distribución de Longitudes de Sépalos
```python
import plotly.express as px

fig = px.histogram(df, x="sepal length (cm)", title="Distribución de Longitudes de Sépalos")
fig.show()
```

### Gráfico de Dispersión de Longitudes y Anchuras de Pétalos
```python
import plotly.express as px

fig = px.scatter(df, x="petal length (cm)", y="petal width (cm)", title="Relación entre Longitudes y Anchuras de Pétalos")
fig.show()
```

Estas visualizaciones permiten explorar la distribución de las longitudes de sépalos y la relación entre las longitudes y anchuras de pétalos.