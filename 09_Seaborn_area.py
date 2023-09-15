import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\automobile.csv')
df = df.dropna(axis=0)

# Genera el gráfico
sns.lineplot(x='horsepower', y='price', data=df)
plt.fill_between(df['horsepower'], df['price'], color='blue', alpha=0.2)  # Agregar un área sombreada debajo de la línea
plt.show()
