import streamlit as st

def columnas():
    columnador = {
    }
    for i in range(1, 9):
        col1, col2 = st.columns(2)
        columnador[f"graph{i}"] = (col1, col2)

    return columnador
def estilo1(fig):
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    fig.update_layout(
        title=dict(
            font=dict(size=24),
            x=0.5,
            xanchor="center",
            y=0.95,
            yanchor="top"
        )
    )
    return fig

