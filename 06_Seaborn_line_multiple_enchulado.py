import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\automobile.csv')
df = df.dropna(axis=0)

# Crear el gráfico con un solo llamado a sns.lineplot()
plt.figure(figsize=(10, 6))  # Ajustar el tamaño de la figura

sns.lineplot(x='horsepower', y='price', data=df, color='blue', label='Horsepower')
sns.lineplot(x='engine-size', y='price', data=df, color='green', label='Engine Size')
sns.lineplot(x='curb-weight', y='price', data=df, color='red', label='Curb Weight')

# Personalizar el gráfico
plt.title('Relación entre Características y Precio de Automóviles', fontsize=16)
plt.xlabel('Característica', fontsize=12)
plt.ylabel('Precio (Dólares)', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Agregar una cuadrícula
plt.grid(True, linestyle='--', alpha=0.6)

# Agregar una leyenda
plt.legend(loc='best', fontsize=12)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
