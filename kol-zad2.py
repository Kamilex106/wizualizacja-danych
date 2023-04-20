def func_1(t):
    unique_elements = set(t)
    for element in unique_elements:
        print(element)

a = (3, 2, 5, 3)
func_1(a)

def func_2(n):
    if n in [0, 1, 2]:
        return 1
    else:
        return 2 * func_2(n - 1) + func_2(n - 2) - func_2(n - 3)

print(func_2(19))


def func_3(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(func_3(5, 2, 7))


text = "I study at the University of Warmia and Mazury in Olsztyn"
reversed_text = text[::-1]
print(reversed_text[::3])


fruits = ['apple', 'banana', 'pomergranate', 'plum', 'orange', 'melon', 'cherry', 'watermelon']
filtered_fruits = [fruit for fruit in fruits if 'l' in fruit and 'a' in fruit]
print(filtered_fruits)


class Frac:
    def __init__(self, num, den):
        gcd = self.gcd(num, den)
        self.num = num // gcd
        self.den = den // gcd

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Frac(num, den)

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        return Frac(num, den)

    def __gt__(self, other):
        return self.num * other.den > self.den * other.num

print(Frac(2, 6) + Frac(1, 5))
print(Frac(3, 6) > Frac(1, 3))
