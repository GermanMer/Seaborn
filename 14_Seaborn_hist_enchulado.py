import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\automobile.csv')
df = df.dropna(axis=0)

# Personalizar el estilo de Seaborn
sns.set(style="whitegrid")

# Crear el gráfico de histograma
bins = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000] #Acá se ponen los valores para los límites de los bins
sns.histplot(df['price'], bins=bins, kde=True, color='skyblue', edgecolor='black')

# Personalizar el gráfico
plt.title('Distribución de Precios de Automóviles', fontsize=16)
plt.xlabel('Precio (Dólares)', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Agregar una cuadrícula
plt.grid(True, linestyle='--', alpha=0.6)

# Agregar una línea vertical para la media del precio
mean_price = df['price'].mean()
plt.axvline(mean_price, color='red', linestyle='--', label=f'Media: ${mean_price:.2f}')
plt.legend()

# Mostrar el gráfico
plt.show()
