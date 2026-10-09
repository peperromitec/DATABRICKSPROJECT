import streamlit as st
from graphs import cargar_bd,plot_1_barras
from dictionary import columnas

st.set_page_config(page_title = "Encuesta Dominio IA", layout = "wide")
st.title("Dashboard EDA🦧🤖")
#=====CARGAR FUNCIONES==========================
columnador = columnas()
df = cargar_bd()

#=========================================================
with columnador["graph1"][0]:
    fig, metricas = plot_1_barras(df)
    st.plotly_chart(fig, use_container_width=True)
with columnador["graph1"][1]:
    st.subheader("Productos más solicitados")
    st.metric("Total de productos", metricas['frecuencia'].sum())
    st.metric("Otros productos", 1000 - abs(metricas['frecuencia'].sum()))
st.divider()

# #=========================================================
# st.subheader("GRAPH 2")
# with col3:
#     st.write("texto")
# with col4:
#     st.write("texto")
# st.divider()
# #=========================================================
# st.subheader("GRAPH 3")
# with col5:
#     st.write("texto")
# with col6:
#     st.write("texto")
# st.divider()
# #=========================================================
# st.subheader("GRAPH 4")
# with col7:
#     st.write("texto")
# with col8:
#     st.write("texto")
# st.divider()
# #=========================================================
# st.subheader("GRAPH 5")
# with col9:
#     st.write("texto")
# with col10:
#     st.write("texto")
# st.divider()
# #=========================================================
# st.subheader("GRAPH 6")
# with col11:
#     st.write("texto")
# with col12:
#     st.write("texto")
# #=========================================================
# st.divider()
# st.subheader("GRAPH 7")
# with col13:
#     st.write("texto")
# with col14:
#     st.write("texto")
# #=========================================================
# st.divider()
# st.subheader("GRAPH 8")
# with col15:
#     st.write("texto")
# with col16:
#     st.write("texto")
# #=========================================================
