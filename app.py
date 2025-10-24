# Aplicación web usando Dash
# Autor: Joan Sebastian Talaga Ospina


# Importamos las librerías necesarias
import plotly.express as px
from dash import Dash, dcc, html

# Iniciamos la aplicación
app = Dash()

# Gráfico 1: Pastel con datos de tips (Datos sobre propinas)
datos_tips = px.data.tips()
mi_figura_pie = px.pie(datos_tips, names="sex", values="tip", title="Distribución de propinas por sexo")


# Gráfico 2: Barras con datos de gapminder
datos_gap = px.data.gapminder()
# Filtramos un año para que el gráfico sea más claro (por ejemplo, 2007)
datos_2007 = datos_gap[datos_gap["year"] == 2007]


# Creamos el gráfico de barras
mi_figura_barras = px.bar(
    datos_2007,
    x="continent",  #Continente
    y="gdpPercap",   # PIB per Capita
    color="continent", #Diferentes colores a cada barra
    title="PIB per cápita por continente en 2007" #Titulo de la imagen
)
# La estructura visual de la aplicación se define dentro de app.layout
# Usamos un html.Div() que agrupa todos los elementos en una sola columna

app.layout = html.Div([
    html.H1("Aplicación usando Dash"),
    dcc.Graph(figure=mi_figura_pie),
    dcc.Graph(figure=mi_figura_barras)
])

# Ejecutamos la app
app.run(debug=True, use_reloader=False)
