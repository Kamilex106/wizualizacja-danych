import seaborn as sns
import matplotlib.pyplot as plt

# Ładowanie danych
penguins = sns.load_dataset("penguins")

# Tworzenie wykresu punktowego
sns.scatterplot(data=penguins, x="bill_length_mm", y="bill_depth_mm",
                hue="species", size="body_mass_g", style="island")

# Wyświetlanie wykresu
plt.show()
