sentence = "I study at the University of Warmia and Mazury in Olsztyn"
no_spaces = sentence.replace(" ", "")
substring = no_spaces[4:40:4]
print(substring)


def func_3(*args):
    product = 1
    for num in args:
        product *= num
    return product / len(args)

print(func_3(10, 9, 2))


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


squares = [x**2 for x in range(1, 16)]
even_squares_factorials = [factorial(sq) for sq in squares if sq % 2 == 0]
print(even_squares_factorials)


def geometric_sequence(n, a1=1, q=2):
    return a1 * (q ** (n - 1))

# Test cases
print(geometric_sequence(4))
print(geometric_sequence(4, a1=3, q=3))


class Frac:
    def __init__(self, num, den):
        self.num = num
        self.den = den
        self._simplify()

    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def _simplify(self):
        common_divisor = self._gcd(self.num, self.den)
        self.num //= common_divisor
        self.den //= common_divisor

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Frac(num, den)

    def __pow__(self, power):
        return Frac(self.num ** power, self.den ** power)

    def __ge__(self, other):
        return (self.num * other.den) >= (self.den * other.num)

# Przykładowe użycie
print(Frac(2, 10) ** 2)
print(Frac(2, 10) >= (-Frac(1, 5)))
