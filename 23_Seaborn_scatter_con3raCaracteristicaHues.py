import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\automobile.csv')
df = df.dropna(axis=0)

# Genera el gráfico
sns.scatterplot(x='horsepower', y='price', hue='engine-size', data=df)
plt.show()
