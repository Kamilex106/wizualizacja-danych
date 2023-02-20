import math
## a)
n =0
n = input("podaj liczbe calkowita n:")
i=1

if int(n)>0 and int(n)<100:
    while i <= int(n):
        print(int(i) * int(i))
        i += 1
else:
    print("n is too large")

## b)
a = input("podaj a")
b = input("podaj b")
nwd = math.gcd(int(a),int(b))
p = (int(a)/nwd)
q = (int(b)/nwd)
print("p:",int(p))
print("q:",int(q))
##c)
def funkcja(n):
    e1 = (1+(1/n))**n
    print(e1)
    sum = 0
    k = 0
    for i in range(k, n + 1):
        sum += 1/math.factorial(i)
    e2 = sum
    return e2

print(funkcja(1000))
print(math.e)

## d)
def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    return a