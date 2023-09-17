import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\automobile.csv')
df = df.dropna(axis=0)

# Crear el gráfico de dispersión con colores basados en 'engine-size'
sns.scatterplot(x='horsepower', y='price', hue='engine-size', data=df)

# Trazar la regresión lineal
sns.regplot(x='horsepower', y='price', data=df, scatter=False)

plt.show()
