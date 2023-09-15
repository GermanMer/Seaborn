import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\migration.csv')
df = df.dropna(axis=0)
df['Value'] = df['Value'].astype(int)
argentina = df[(df['Country of birth/nationality'] == 'Argentina') & (df['Country'] == 'Spain')]
argentina = argentina.groupby('Year')['Value'].sum().reset_index()

# Crear el gráfico de línea
sns.lineplot(x='Year', y='Value', data=argentina, label='De Argentina hacia España')
plt.show()
