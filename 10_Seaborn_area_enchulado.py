import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\automobile.csv')
df = df.dropna(axis=0)

# Personalizar el estilo de Seaborn
sns.set(style="whitegrid")

# Crear un gráfico de área personalizado
sns.lineplot(x='horsepower', y='price', data=df, ci=None, color='blue', label='Precio vs Potencia')
plt.fill_between(df['horsepower'], df['price'], color='blue', alpha=0.2)  # Agregar un área sombreada debajo de la línea

# Personalizar el gráfico
plt.title('Relación entre Potencia y Precio de Automóviles', fontsize=16)
plt.xlabel('Potencia (Horsepower)', fontsize=12)
plt.ylabel('Precio (Dólares)', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Agregar una cuadrícula
plt.grid(True, linestyle='--', alpha=0.6)

# Agregar una leyenda
plt.legend(loc='best', fontsize=12)

# Mostrar el gráfico
plt.show()
