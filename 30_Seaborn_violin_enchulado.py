import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\automobile.csv')
df = df.dropna(axis=0)

# Personalizar el estilo de Seaborn
sns.set(style="whitegrid")

# Crear el gráfico de violín
sns.violinplot(x='body-style', y='price', data=df, palette='Set2', inner='quartile', scale='width')

# Personalizar el gráfico
plt.title('Distribución de Precios por Estilo de Carrocería', fontsize=16)
plt.xlabel('Estilo de Carrocería', fontsize=12)
plt.ylabel('Precio (Dólares)', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
