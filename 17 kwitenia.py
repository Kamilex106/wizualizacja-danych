
#cw1
# def print_unique_values(lst):
#     for value in set(lst):
#         print(value)
#
#
# print_unique_values([1,2,2,5,6,1])


#cw2
# def print_every_fourth_letter_in_reverse(word):
#     word = word.replace(" ", "")
#     word = ''.join(filter(str.isalpha, word))
#     for i in range(len(word)-1, -1, -4):
#         print(word[i])
#
#
# def wyswietl_co_czwarta_odwrotnie(tekst):
#     tekst_bez_spacji = tekst.replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "")
#     odwrocony_tekst = tekst_bez_spacji[::-1]
#     for i in range(0, len(odwrocony_tekst), 4):
#         print(odwrocony_tekst[i])

# print_every_fourth_letter_in_reverse("pyt5on")
# print("\n")
# zmienna = "witaj, świecie! Spróbujmy zrozumieć pythona."
# wyswietl_co_czwarta_odwrotnie(zmienna)
# print("\n")
# wyswietl_co_czwarta_odwrotnie("Alamakota")

#cw3
# def fibonacci_recursive(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
#
# print(fibonacci_recursive(6))
#
# def fibonacci_iterative(n):
#     if n <= 1:
#         return n
#     else:
#         a = 0
#         b = 1
#         for i in range(2, n+1):
#             c = a + b
#             a = b
#             b = c
#         return b
#
# print(fibonacci_iterative(6))

#
#cw4

# def product_of_nth_powers(n, *args):
#     product = 1
#     for arg in args:
#         product *= arg ** n
#     return product
#
# print(product_of_nth_powers(2, 1, 2, 3))


#cw5

# fruits = ['apple', 'banana', 'pomergranate', 'plum', 'orange', 'melon', 'cherry', 'watermelon']
# result = [len(fruit) for fruit in fruits if 'u' in fruit or 'o' in fruit]
# print(result)

#cw6
# def newton_symbol(n, k):
#     if k == 0 or k == n:
#         return 1
#     else:
#         return newton_symbol(n-1, k-1) + newton_symbol(n-1, k)
#
# print(newton_symbol(5, 2))
#
#
# def newton_symbol(n, k):
#     def factorial(number):
#         if number == 0 or number == 1:
#             return 1
#         else:
#             return number * factorial(number - 1)
#
#     if n < k or n < 0 or k < 0:
#         return "Podano niepoprawne wartości n i k"
#     else:
#         return factorial(n) // (factorial(k) * factorial(n - k))
#
# # Przykład użycia funkcji
# n = 5
# k = 2
# result = newton_symbol(n, k)
# print(f"Wartość symbolu Newtona dla n={n} i k={k} wynosi: {result}")
# print("Wartość symbolu Newtona dla n=",n,"i k=",k,"wynosi:",result)

#cw7
# class Polynomial:
#     def __init__(self, coeffs):
#         self.coeffs = coeffs
#
#     def degree(self):
#         return len(self.coeffs) - 1
#
#     def __add__(self, other):
#         result_coeffs = []
#         min_degree = min(self.degree(), other.degree())
#         for i in range(min_degree + 1):
#             result_coeffs.append(self.coeffs[i] + other.coeffs[i])
#         result_coeffs.extend(self.coeffs[min_degree + 1:])
#         result_coeffs.extend(other.coeffs[min_degree + 1:])
#         return Polynomial(result_coeffs)
#
#     def __sub__(self, other):
#         result_coeffs = []
#         min_degree = min(self.degree(), other.degree())
#         for i in range(min_degree + 1):
#             result_coeffs.append(self.coeffs[i] - other.coeffs[i])
#         result_coeffs.extend(self.coeffs[min_degree + 1:])
#         for c in other.coeffs[min_degree + 1:]:
#             result_coeffs.append(-c)
#         return Polynomial(result_coeffs)
#
#     def __getitem__(self, index):
#         if index > self.degree():
#             return 0
#         return self.coeffs[index]
#
#     def __str__(self):
#         terms = []
#         for i, coeff in enumerate(self.coeffs[::-1]):
#             if coeff == 0:
#                 continue
#             term = f'{coeff:+}' if i != 0 else f'{coeff}'
#             if i > 0:
#                 term += f'x^{len(self.coeffs) - i}'
#             terms.append(term)
#         return ' '.join(terms)
#
# # Przykład użycia
# p1 = Polynomial([2, -2, 1])
# p2 = Polynomial([1, 2, 3])
# print("p1:", p1)
# print("p2:", p2)
# print("p1 + p2:", p1 + p2)
# print("p1 - p2:", p1 - p2)
#


class Polynomial:
    def __init__(self,coef):
        self.coef = coef

    def __str__(self):
        s = ""
        for i in range(len(self.coef)-1,0,1):
            s+=str(self.coef[i])+("x^")+str(i)+"+"
        s += str(self.coef[0])
        return (s)


    def __add__(self, other):
        s = []
        l1 = self.coef
        l2 = other.coef
        if (len(l1)>len(l2)):
            for i in range(0,len(l1)-len(l2)):
                l2.append(0)
        else:
            for i in range(0,len(l2)-len(l1)):
                l1.append(0)
        return [x+y for x,y in zip(l1,l2)]

        print(l2)
        for i in range(0,min(len(self.coef),len(other.coef))):
            s.append(self.coef[i]+other.coef[i])



a = Polynomial([2,3,4])
b = Polynomial([1,4,2,2])
print(a+b)