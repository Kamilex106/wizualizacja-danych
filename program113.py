import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Wczytanie danych z pliku CSV
data = pd.read_csv('iris.csv')

# Wykres zależności punktowej
plt.scatter(data['sepal_length'], data['sepal_width'], c=data['species'].map({'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}))
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')
plt.title('Zależność punktowa - sepal_length vs sepal_width')
plt.show()



# Catplot - różne wartości od gatunków
sns.catplot(x='species', y='petal_length', data=data, kind='violin')
plt.xlabel('species')
plt.ylabel('petal_length')
plt.title('Wartość petal_length dla poszczególnych gatunków')
plt.show()

sns.catplot(x='species', y='petal_width', data=data, kind='violin')
plt.xlabel('species')
plt.ylabel('petal_width')
plt.title('Wartość petal_width dla poszczególnych gatunków')
plt.show()

sns.catplot(x='species', y='sepal_length', data=data, kind='violin')
plt.xlabel('species')
plt.ylabel('sepal_length')
plt.title('Wartość sepal_length dla poszczególnych gatunków')
plt.show()





# Pairplot
sns.pairplot(data, hue='species')
plt.show()
