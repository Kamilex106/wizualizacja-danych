string = "abcdefghijklmnoprstuwxyz"
print(string[9::2])

def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return 3 * fibonacci(n - 1) + 2 * fibonacci(n - 2)

print(fibonacci(14))

words1 = ["kot", "pies", "lama", "aligator", "krokodyl"]
result1 = [len(word) for word in words1 if "l" in word and "a" in word]
print(result1)

words2 = ["jabłko", "gruszka", "banan", "ananas"]
result2 = [len(word) for word in words2 if "l" in word and "a" in word]
print(result2)

def average(*args):
    if len(args) == 0:
        return None
    else:
        product = 1
        for arg in args:
            product *= arg
        return product / len(args)

result = average(10,9,2)
print(result)


def number_to_text(number):
    digits = {
        "0": "zero",
        "1": "jeden",
        "2": "dwa",
        "3": "trzy",
        "4": "cztery",
        "5": "pięć",
        "6": "sześć",
        "7": "siedem",
        "8": "osiem",
        "9": "dziewięć"
    }
    result = ""
    for char in number:
        if char.isdigit():
            result += digits[char] + " "
    return result.strip()

result = number_to_text("45j2")
print(result)

def temperature_converter(temperature, scale):
    if scale == "C":
        celsius = temperature
        kelvin = temperature + 273.15
        fahrenheit = (temperature * 9/5) + 32
    elif scale == "K":
        celsius = temperature - 273.15
        kelvin = temperature
        fahrenheit = (temperature - 273.15) * 9/5 + 32
    elif scale == "F":
        celsius = (temperature - 32) * 5/9
        kelvin = (temperature - 32) * 5/9 + 273.15
        fahrenheit = temperature
    else:
        return None

    result = f"{celsius:.2f}°C, {kelvin:.2f}K, {fahrenheit:.2f}°F"
    return result

result = temperature_converter(25, "C")
print(result)



class Frac:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Frac(numerator, denominator)

    def __pow__(self, power):
        numerator = self.numerator ** power
        denominator = self.denominator ** power
        return Frac(numerator, denominator)

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

result = Frac(2, 6) * Frac(1, 5)
print(result)

result = Frac(2, 6) == Frac(1, 3)
print(result)