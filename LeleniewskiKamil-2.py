#Kamil Leleniewski, 169327, wariant 14
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


#zad.1

# Nazwy rzek
nazwy_rzek = np.array([
    'Amazonka', 'Nil', 'Jangcy', 'Missisipi-Missouri', 'Huang He',
    'Ob Irtysz', 'Kongo', 'Mekong', 'Amur', 'Lena', 'Parana',
    'Mackanzie', 'Niger', 'Jenisej', 'Wotga'
])

# Kontynenty
kontynenty = np.array([
    'Ameryka Południowa', 'Afryka', 'Eurazja', 'Ameryka Północna', 'Eurazja',
    'Eurazja', 'Afryka', 'Eurazja', 'Eurazja', 'Eurazja', 'Ameryka Południowa',
    'Ameryka Północna', 'Afryka', 'Eurazja', 'Eurazja'
])

# Długość w km
dlugosc = np.array([
    7040, 6695, 6300, 6020, 5464,
    5410, 4700, 4500, 4440, 4400, 4380,
    4240, 4160, 4102, 3530
])

# Powierzchnia dorzecza w tys. km2
powierzchnia = np.array([
    7200, 2870, 1807, 3229, 752,
    2972, 3690, 810, 1855, 2490, 3100,
    1760, 2117, 2580, 1360
])

# Liczba państw przez które przepływa
liczba_panstw = np.array([
    3, 7, 1, 1, 1,
    3, 3, 6, 3, 1, 3,
    1, 4, 2, 2
])

# Ile rzek jest w tabelce?
liczba_rzek = len(nazwy_rzek)
print("Liczba rzek w tabelce:", liczba_rzek)

# Które rzeki przepływają przez dokładnie 3 państwa?
rzeki_3_panstwa = nazwy_rzek[liczba_panstw == 3]
print("Rzeki przepływające przez dokładnie 3 państwa:", rzeki_3_panstwa)

# Ile rzek ma długość mniejszą niż 5000 km?
rzeki_krotsze_5000km = len(dlugosc[dlugosc < 5000])
print("Liczba rzek o długości mniejszej niż 5000 km:", rzeki_krotsze_5000km)

# Wypisz rzeki, których nazwy zaczynają się od litery 'M'
rzeki_z_litera_M = nazwy_rzek[np.char.startswith(nazwy_rzek, 'M')]
print("Rzeki, których nazwy zaczynają się od litery 'M':", rzeki_z_litera_M)

# Posortuj nazwy rzek według powierzchni malejąco
rzeki_posortowane_powierzchnia = nazwy_rzek[np.argsort(powierzchnia)[::-1]]
print("Posortowane nazwy rzek według powierzchni malejąco:", rzeki_posortowane_powierzchnia)

# Wypisz nazwy rzek z powierzchnią większą niż 2000 tys. km2, które są w Ameryce (Południowej i Północnej)
rzeki_ameryka_powierzchnia = nazwy_rzek[(powierzchnia > 2000) & ((kontynenty == 'Ameryka Południowa') | (kontynenty == 'Ameryka Północna'))]
print("Nazwy rzek z powierzchnią większą niż 2000 tys. km2 w Ameryce:", rzeki_ameryka_powierzchnia)



#zad2


x = np.linspace(-1, 3, 100)
y = np.e**x
y1 = np.e**(2*x)

fig, axs = plt.subplots(2, 1, sharex=True)

axs[0].plot(x, y, 'blue', linestyle="-")
axs[0].set_xlabel('')
axs[0].set_ylabel('')


axs[1].plot(x, y1, 'green', linestyle="--")
axs[1].set_xlabel('')
axs[1].set_ylabel('')

legend_labels = ['e^x', 'e^(2x)']
fig.legend(legend_labels, loc='center', title='Wykres')

plt.tight_layout()

plt.show()



##zad3

# Pobierz i wczytaj plik diamonds.csv
data = pd.read_csv('diamonds.csv')

# Jaka jest średnia cena (price) diamentu typu 'Premium'?
premium_avg_price = data[data['cut'] == 'Premium']['price'].mean()
print("Średnia cena diamentu typu 'Premium':", premium_avg_price)

# Wypisz wszystkie informacje o największym (carat) diamentu koloru 'E'
largest_e_diamond = data[data['color'] == 'E'].nlargest(1, 'carat')
print("Informacje o największym diamentu koloru 'E':")
print(largest_e_diamond)

# Narysuj wykres słupkowy zależności średniej ceny od typu ('cut')
mean_price_by_cut = data.groupby('cut')['price'].mean()
mean_price_by_cut.plot(kind='bar')
plt.xlabel('Cut')
plt.ylabel('Mean Price')
plt.title('Mean Price by Cut')
plt.show()

# Narysuj wykres punktowy zależności ceny(price) od rozmiaru (carat) diamentu,
# kolorem zaznacz kolor diamentu
colors = {'D': 'darkblue', 'E': 'yellow', 'F': 'purple', 'G': 'green',
          'H': 'black', 'I': 'orange', 'J': 'red'}
plt.scatter(data['carat'], data['price'], c=data['color'].map(colors))
plt.xlabel('Carat')
plt.ylabel('Price')
plt.title('Price vs. Carat with Color')
plt.show()



##zad4

data = sns.load_dataset('attention')
sns.boxplot(x='attention', y='score', hue='subject', data=data, palette='Blues')
plt.xlabel('attention')
plt.ylabel('score')
plt.legend(title='Temat')
plt.show()


