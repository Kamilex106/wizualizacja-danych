# Kamil Leleniewski 169327 Wariant 5
#zad1 krotki bez powtórzeń
def func_1(tup):
    unique_tup = set(tup)
    for elem in unique_tup:
        print(elem)

a = (3, 2, 5, 3)
func_1(a)

print("\n")

#zad2 nieparzyste litery w odwrotnym porządku
text = "I study at the University of Warmia and Mazury in Olsztyn"
rev_chars = text.replace(" ", "")[::-1][1::2]
print(rev_chars)


print("\n")

#zad3 rekurencja
def func_2(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return 2 * func_2(n - 1) + func_2(n - 2) - func_2(n - 3)

print(func_2(19))

print("\n")

#zad4 iloczyn
def func_3(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(func_3(5, 2, 7))

print("\n")

#zad5 kwadraty parzystych
kwadraty_parzystych = [x**2 for x in range(2, 51, 2)]
print(kwadraty_parzystych)

print("\n")

#
#zad6 szyfr
klucz = {'a': 'y', 'e': 'i', 'i': 'o', 'o': 'a', 'y': 'e'}

def encrypt(text):
    return "".join([klucz.get(char, char) for char in text])


def decrypt(text):
    reverse_key = {v: k for k, v in klucz.items()}
    return "".join([reverse_key.get(char, char) for char in text])

word = "informatyka"
encrypted_word = encrypt(word)
print(encrypted_word)

decrypted_word = decrypt(encrypted_word)
print(decrypted_word)

print("\n")


#zad7 liczby wymierne
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


class Frac:
    def __init__(self, num, den):
        common_factor = gcd(num, den)
        self.num = num // common_factor
        self.den = den // common_factor

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __sub__(self, other):
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        return Frac(num, den)

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        return Frac(num, den)

    def __eq__(self, other):
        return self.num == other.num and self.den == other.den

# frac1 = Frac(2, 6)
# frac2 = Frac(1, 5)
# print(frac1 - frac2)
# print(frac1 == Frac(1, 3))

print(Frac(1,5))
print(Frac(5,10)*Frac(1,2))
print(Frac(10,10)-Frac(2,5))
print("\n")
print(Frac(2,6)-Frac(1,5))
print(Frac(2,6)==Frac(1,3))