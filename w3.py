def dict0(dictionary):
    for key in dictionary.keys():
        print(key)

dict = {'a':1, 'b':2, 'c':3, 'd':4}
dict0(dict)


text = "I study at the University of Warmia and Mazury in Olsztyn"
text = text.replace(" ", "")
result = text[5:40:4]
print(result)

def func3(*args):
    product = 1
    for arg in args:
        product *= arg
    return product / len(args)

print(func3(10,9,2))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

squares = [x**2 for x in range(1, 16) if x % 2 == 0]
factorials = [factorial(x) for x in squares]

print(factorials)

def geometric_sequence_element(n, a1=1, q=2):
    return a1 * q**(n-1)

result = geometric_sequence_element(4, 3, 3)
print(result)
# 81

result = geometric_sequence_element(5, 2, 2)
print(result)
# 32

class Frac:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if isinstance(other, Frac):
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Frac(new_numerator, new_denominator)
        else:
            raise TypeError("Can only add Frac to another Frac")

    def __pow__(self, power):
        if isinstance(power, int) and power >= 0:
            return Frac(self.numerator ** power, self.denominator ** power)
        else:
            raise TypeError("Power must be a non-negative integer")

    def __ge__(self, other):
        if isinstance(other, Frac):
            return self.numerator * other.denominator >= other.numerator * self.denominator
        else:
            raise TypeError("Can only compare Frac to another Frac")

print(Frac(2,10)**2)
print(Frac(2,10)>=Frac(1,5))