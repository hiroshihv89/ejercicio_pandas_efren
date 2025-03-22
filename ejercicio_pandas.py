import pandas as pd
import os

# Cargar el archivo CSV en un DataFrame, ruta relativa para que funcione en cualquier PC
archivo_csv = "empleados.csv"
if not os.path.exists(archivo_csv):
    raise FileNotFoundError(f"El archivo {archivo_csv} no se encuentra en el directorio actual.")

df = pd.read_csv(archivo_csv)

# Mostrar los primeros 10 registros
print("Primeros 10 registros:")
print(df.head(10))

# Obtener resumen estadístico de las columnas numéricas
print("\nResumen estadístico:")
print(df.describe())

# Filtrar empleados con salario mayor a 5000
empleados_salario_alto = df[df['Salario'] > 5000]
print("\nEmpleados con salario mayor a 5000:")
print(empleados_salario_alto)

# Crear nueva columna 'Alto_Desempeño'
df['Alto_Desempeño'] = df['Evaluacion_Desempeño'] > 4
print("\nColumna 'Alto_Desempeño' creada.")

# Eliminar la columna 'Bono_Anual'
if 'Bono_Anual' in df.columns:
    df.drop(columns=['Bono_Anual'], inplace=True)
    print("\nColumna 'Bono_Anual' eliminada.")

# Calcular total de salarios por departamento
salario_por_departamento = df.groupby('Departamento')['Salario'].sum()
print("\nTotal de salarios por departamento:")
print(salario_por_departamento)

# Encontrar el empleado más joven
empleado_mas_joven = df[df['Edad'] == df['Edad'].min()]
print("\nEmpleado más joven:")
print(empleado_mas_joven)

# Encontrar el empleado con más años de experiencia
empleado_mas_experiencia = df[df['Años_Experiencia'] == df['Años_Experiencia'].max()]
print("\nEmpleado con más años de experiencia:")
print(empleado_mas_experiencia)

# Manejo de valores nulos en 'Proyectos_Completados'
if df['Proyectos_Completados'].isnull().sum() > 0:
    promedio_proyectos = df['Proyectos_Completados'].mean()
    df['Proyectos_Completados'] = df['Proyectos_Completados'].fillna(promedio_proyectos)
    print("\nValores nulos en 'Proyectos_Completados' reemplazados por el promedio.")

# Guardar el DataFrame modificado en un nuevo archivo CSV
archivo_modificado = "empleados_modificado.csv"
df.to_csv(archivo_modificado, index=False)
print(f"\nDatos modificados guardados en {archivo_modificado}")
