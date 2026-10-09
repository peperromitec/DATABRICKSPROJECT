import os
import pandas as pd
from pyspark.sql.functions import col

# 1. Conexión al Workspace de Databricks
os.environ["DATABRICKS_HOST"] = "https://dbc-eb20e297-b998.cloud.databricks.com"
from databricks.connect import DatabricksSession

print("Conectando con Databricks...")
spark = DatabricksSession.builder.serverless(True).getOrCreate()

# 2. Si ya te dieron permisos en 'tld_silver', déjalo así. 
# Si no, puedes probar con "samples.nyctaxi.trips" para verificar tus gráficas.
tabla_path = "workspace.default.tld_silver"

print(f"Consultando datos filtrados de {tabla_path}...")

# 3. Cargamos la tabla y filtramos de forma correcta usando 'col()'
df_spark = spark.table(tabla_path)
df_filtrado = df_spark.filter(
    (col("total") >= 20)
)

# 4. Limitamos a 1000 registros y bajamos a Pandas
df_pd = df_filtrado.limit(1000).toPandas()

# 5. Guardar los datos para tu EDA
print("¡Datos descargados con éxito!")
print(df_pd.head())
df_pd.to_csv("datos_filtrados.csv", index=False)
print("¡Guardado en 'datos_filtrados.csv'!")