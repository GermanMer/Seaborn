import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\automobile.csv')
df = df.dropna(axis=0)

# Personalizar el estilo de Seaborn
sns.set(style="whitegrid")

# Crear el gráfico de dispersión con colores basados en 'engine-size'
sns.scatterplot(x='horsepower', y='price', hue='engine-size', data=df, palette='coolwarm', s=80, alpha=0.7)

# Agregar una leyenda para 'engine-size'
plt.legend(title='Tamaño del Motor', fontsize=10, title_fontsize=12)

# Trazar la regresión lineal
sns.regplot(x='horsepower', y='price', data=df, scatter=False, color='blue', line_kws={'color': 'red', 'linestyle': '--'})

# Personalizar el gráfico
plt.title('Relación entre Potencia, Precio y Tamaño del Motor', fontsize=16)
plt.xlabel('Potencia (Horsepower)', fontsize=12)
plt.ylabel('Precio (Dólares)', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
