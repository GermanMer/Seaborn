import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\automobile.csv')
df = df.dropna(axis=0)

# Personalizar el estilo de Seaborn
sns.set(style="whitegrid")

# Crear el gráfico de caja
sns.boxplot(y='price', data=df, palette='Set3')  # Utiliza una paleta de colores personalizada

# Personalizar el gráfico
plt.title('Distribución del Precio de los Automóviles', fontsize=16)
plt.xlabel('Automóviles', fontsize=12)
plt.ylabel('Precio (Dólares)', fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)

# Agregar líneas adicionales para resaltar valores atípicos (outliers)
sns.stripplot(x='horsepower', y='price', data=df, color='gray', size=4, jitter=True)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
