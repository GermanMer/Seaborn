import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\migration.csv')
df = df.dropna(axis=0)
df['Value'] = df['Value'].astype(int)

arg_esp = df[(df['Country of birth/nationality'] == 'Argentina') & (df['Country'] == 'Spain')]
arg_esp = arg_esp.groupby('Year')['Value'].sum().reset_index()

arg_ita = df[(df['Country of birth/nationality'] == 'Argentina') & (df['Country'] == 'Italy')]
arg_ita = arg_ita.groupby('Year')['Value'].sum().reset_index()

arg_usa = df[(df['Country of birth/nationality'] == 'Argentina') & (df['Country'] == 'United States')]
arg_usa = arg_usa.groupby('Year')['Value'].sum().reset_index()

# Personalizar el estilo de Seaborn
sns.set(style="whitegrid")

# Crear el gráfico de barras
sns.barplot(x='Year', y='Value', data=arg_esp, color='blue', alpha=0.3, label='Hacia España')
sns.barplot(x='Year', y='Value', data=arg_ita, color='green', alpha=0.3, label='Hacia Italia')
sns.barplot(x='Year', y='Value', data=arg_usa, color='red', alpha=0.3, label='Hacia Estados Unidos')

# Personalizar el gráfico
plt.title('Emigración desde Argentina a España, Italia y Estados Unidos', fontsize=16)
plt.xlabel('Año', fontsize=12)
plt.ylabel('Cantidad de Emigrantes', fontsize=12)
plt.xticks(rotation=45, fontsize=10)  # Rotar las etiquetas del eje x para mejor legibilidad
plt.yticks(fontsize=10)

# Agregar una leyenda
plt.legend(loc='best', fontsize=12)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
