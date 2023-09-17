import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\automobile.csv')
df = df.dropna(axis=0)

# Personalizar el estilo de Seaborn
sns.set(style="whitegrid")

# Crear el gráfico de regresión
sns.regplot(x='horsepower', y='price', data=df, color='blue', scatter_kws={'s': 50}, line_kws={'color': 'red', 'linestyle': '--'})

# Personalizar el gráfico
plt.title('Relación entre Potencia y Precio con Regresión', fontsize=16)
plt.xlabel('Potencia (Horsepower)', fontsize=12)
plt.ylabel('Precio (Dólares)', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
