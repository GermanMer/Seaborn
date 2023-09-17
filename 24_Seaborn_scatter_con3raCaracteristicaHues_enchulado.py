import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\automobile.csv')
df = df.dropna(axis=0)

# Personalizar el estilo de Seaborn
sns.set(style="whitegrid")

# Personalizar la paleta de colores para 'engine-size'
palette = 'coolwarm'  # Cambiar la paleta de colores según tus preferencias

# Crear el gráfico de dispersión
sns.scatterplot(x='horsepower', y='price', hue='engine-size', data=df, palette=palette, alpha=0.7, s=80)

# Personalizar el gráfico
plt.title('Relación entre Potencia, Precio y Tamaño del Motor', fontsize=16)
plt.xlabel('Potencia (Horsepower)', fontsize=12)
plt.ylabel('Precio (Dólares)', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Agregar una leyenda
plt.legend(loc='best', title='Tamaño del Motor', fontsize=10, title_fontsize=12)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
