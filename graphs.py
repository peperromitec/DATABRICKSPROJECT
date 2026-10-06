import plotly.express as px
import numpy as np
import pandas as pd
from dictionary import estilo1
def cargar_bd():
    df = pd.DataFrame({
        "category": ["a", "b", "c"],
        "frequency": [4, 5, 6]
    })

    return df
estilo1 = estilo1
def plot_1_barras(df):
    fig = px.bar(
        df,
        x="category",
        y="frequency",
        title="GRÁFICA 1"
    )

    

    return estilo1(fig)
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