class Romanian:
    def __init__(self, value):
        self.value=value
    def on_romanian(self):
        romanian_numbers = (('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50),
                             ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1))
        num = self.value
        result=''
        while num>0:
            for romanian, i in romanian_numbers:
                if num >= i:
                    result += romanian
                    num -= i
                    break
            return result
#wyj.: sprawdza, czy liczba jest większa od zera. Jeśli tak, przechodzi przez krotki
#z liczbami rzymskimi i znajduje największą liczbę rzymską, która jest mniejsza lub równa liczbie.
#Następnie dodaje znak rzymski do wyniku, a wartość liczby rzymskiej odejmuje od liczby arabskiej.
#Proces ten jest powtarzany, aż liczba spadnie do zera. Wtedy metoda zwraca wynik.
    def on_arabian(self):
        romanian_numbers = (('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50),
                            ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1))
        romanian_str = self.value
        i = result = 0
        while i < len(romanian_str):
            for romanian, num in romanian_numbers:
                if romanian_str[i:i + len(romanian)] == romanian:
                    result += num
                    i += len(romanian)
                    break
        return result


a = Romanian(40)
print(a.on_romanian())
