import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\automobile.csv')
df = df.dropna(axis=0)

# Personalizar el estilo de Seaborn
sns.set(style="whitegrid")

# Crear el gráfico de dispersión
sns.scatterplot(x='horsepower', y='price', data=df, color='blue', alpha=0.7, s=80)  # Personaliza color, transparencia y tamaño de puntos

# Personalizar el gráfico
plt.title('Relación entre Potencia y Precio', fontsize=16)
plt.xlabel('Potencia (Horsepower)', fontsize=12)
plt.ylabel('Precio (Dólares)', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Agregar líneas de referencia
sns.regplot(x='horsepower', y='price', data=df, scatter=False, color='red', line_kws={'linestyle': '--'}, ci=None, label='Regresión')

# Mostrar el gráfico
plt.legend(loc='best', fontsize=12)  # Agregar una leyenda
plt.tight_layout()
plt.show()
