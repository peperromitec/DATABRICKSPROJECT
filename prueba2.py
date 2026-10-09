import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Configurar conexión a Databricks
os.environ["DATABRICKS_HOST"] = "https://dbc-eb20e297-b998.cloud.databricks.com"
from databricks.connect import DatabricksSession

spark = DatabricksSession.builder.serverless(True).getOrCreate()

# 2. Consultar la tabla del Unity Catalog compartido y traerla a Pandas
# (Reemplaza con tu catálogo, esquema y el nombre de tu tabla real)
tabla_path = "nombre_de_tu_catalogo.tu_esquema.nombre_de_tu_tabla"

print(f"Descargando datos de {tabla_path}...")
df_spark = spark.table(tabla_path)

# Si la tabla es muy grande, puedes usar .limit(5000) o hacer agregaciones antes de pasarla a Pandas
df_pd = df_spark.limit(5000).toPandas()

# 3. Exploración inicial (EDA)
print("Dimensiones del DataFrame:", df_pd.shape)
print(df_pd.info())
print(df_pd.head())

# 4. GRAFICAR LOS DATOS

# Ejemplo A: Gráfico de correlación (Mapa de calor) si tienes variables numéricas
plt.figure(figsize=(8, 6))
sns.heatmap(df_pd.select_dtypes(include=['number']).corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Matriz de Correlación - EDA Databricks")
plt.show()

# Ejemplo B: Gráfico de distribución de alguna columna clave de tus datos
# (Reemplaza 'columna_numerica' por una columna real de tu base de datos)
# plt.figure(figsize=(8, 5))
# sns.histplot(df_pd['columna_numerica'], kde=True, color='purple')
# plt.title("Distribución de la Variable")
# plt.show()