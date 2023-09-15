import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\migration.csv')
df = df.dropna(axis=0)
df['Value'] = df['Value'].astype(int)

# Filtrar datos para cada destino
arg_esp = df[(df['Country of birth/nationality'] == 'Argentina') & (df['Country'] == 'Spain')]
arg_ita = df[(df['Country of birth/nationality'] == 'Argentina') & (df['Country'] == 'Italy')]
arg_usa = df[(df['Country of birth/nationality'] == 'Argentina') & (df['Country'] == 'United States')]

# Crear el gráfico utilizando Seaborn
plt.figure(figsize=(10, 6))  # Ajustar el tamaño de la figura
sns.lineplot(x='Year', y='Value', data=arg_esp, label='Hacia España', color='blue', marker='o')
sns.lineplot(x='Year', y='Value', data=arg_ita, label='Hacia Italia', color='green', linestyle='--', marker='s')
sns.lineplot(x='Year', y='Value', data=arg_usa, label='Hacia Estados Unidos', color='red', linestyle=':', marker='^')

# Personalizar el gráfico
plt.grid(True)  # Agregar una cuadrícula al gráfico
plt.xlabel('Año')
plt.ylabel('Cantidad de Emigrantes')
plt.title('Emigración Argentina a España, Italia y Estados Unidos')
plt.legend()
plt.tight_layout()  # Ajustar el diseño para evitar recortes en las etiquetas
plt.show()
