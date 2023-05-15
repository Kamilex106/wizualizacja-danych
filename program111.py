import pandas as pd
import matplotlib.pyplot as plt

# Wczytanie pliku CSV do obiektu DataFrame
df = pd.read_csv('penguins.csv')

# Oblicz średnią wagę dla każdej płci i gatunku osobno
mean_weight_sex_species = df.groupby(['species', 'sex'])['body_mass_g'].mean()
print('Średnia waga dla każdej płci i gatunku osobno:')
print(mean_weight_sex_species)

# Znajdź wiersze z największą i najmniejszą wagą
max_weight_penguins = df.nlargest(1, 'body_mass_g')
min_weight_penguins = df.nsmallest(1, 'body_mass_g')
print('\nPingwiny z największą wagą:')
print(max_weight_penguins)
print('\nPingwiny z najmniejszą wagą:')
print(min_weight_penguins)

# Oblicz ilość pingwinów z wyspy Torgersen oraz z każdej innej wyspy
count_by_island = df.groupby('island').size()
count_torgersen = count_by_island['Torgersen']
print('\nIlość pingwinów z wyspy Torgersen:', count_torgersen)
print('\nIlość pingwinów na każdej z wysp:')
print(count_by_island)

# Narysuj wykres słupkowy ilości pingwinów w zależności od wyspy
count_by_island.plot(kind='bar')
plt.show()

# Narysuj wykres punktowy (scatter) zależności długości dzioba od szerokości
size = df['body_mass_g']/2000
colors = {'Adelie':'blue', 'Chinstrap':'green', 'Gentoo':'red'}
plt.scatter(df['bill_length_mm'], df['bill_depth_mm'], s=size, c=df['species'].map(colors))
plt.show()
