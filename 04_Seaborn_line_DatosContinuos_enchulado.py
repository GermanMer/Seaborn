import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\migration.csv')
df = df.dropna(axis=0)
df['Value'] = df['Value'].astype(int)
argentina = df[(df['Country of birth/nationality'] == 'Argentina') & (df['Country'] == 'Spain')]
argentina = argentina.groupby('Year')['Value'].sum().reset_index()

# Personalizar el estilo de Seaborn
sns.set(style="whitegrid")

# Crear el gráfico de línea
sns.lineplot(x='Year', y='Value', data=argentina, ci=None, color='blue', label='De Argentina hacia España')

# Personalizar el gráfico
plt.title('Emigración de Argentina a España', fontsize=16)
plt.xlabel('Año', fontsize=12)
plt.ylabel('Cantidad de Emigrantes', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Agregar una cuadrícula
plt.grid(True, linestyle='--', alpha=0.6)

# Agregar una leyenda
plt.legend(loc='best', fontsize=12)

# Mostrar el gráfico
plt.show()
