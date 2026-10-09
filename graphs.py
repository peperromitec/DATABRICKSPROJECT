import plotly.express as px
import numpy as np
import pandas as pd
from dictionary import estilo1
def cargar_bd():
    df = pd.read_csv("datos_filtrados.csv")

    return df
estilo1 = estilo1
def plot_1_barras(df):
    conteo = df['menu_item'].value_counts().reset_index()
    conteo.columns = ['menu_item', 'frecuencia']
    conteo = conteo[conteo['frecuencia'] >= 15]
    fig = px.bar(
    conteo,
    x='menu_item',
    y='frecuencia',
    title='Frecuencia de cada elemento del menú',
    labels={
        'menu_item': 'Elemento del menú',
        'frecuencia': 'Cantidad'
    },
    text='frecuencia',
    color='frecuencia',
    color_continuous_scale='Blues'
)

    return estilo1(fig), conteo
def plot_2(df):
    fig = px.bar(
        df,
        x="category",
        y="frequency",
        title="GRÁFICA 1"
    )
    return

def plot_3(df):
    fig = px.bar(
        df,
        x="category",
        y="frequency",
        title="GRÁFICA 1"
    )
    return
def plot_4(df):
    fig = px.bar(
        df,
        x="category",
        y="frequency",
        title="GRÁFICA 1"
    )
    return