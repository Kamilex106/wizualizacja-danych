#Zadanie 1
a = (3,2,5,3)

def func_1(krotka):
    for i in set(krotka):
        print(i)

func_1(a)


#Zadanie 1 inny wariant
dict0 = {"a":"y","e":"i", "i":"o","o":"a", "y":"e"}
def func_sz (napis):
    str0 = ''
    for i in napis:
        if i in dict0.keys():
            str0+=dict0[i]
        else: str0+=i
    return(str0)
print(func_sz ("informatyka"))
#Zadanie 2
def func_2(n):
    if 0 <=n < 3:
        return 1
    else:
        return 2*func_2(n-1)+func_2(n-2)-func_2(n-3)

print(func_2(19))

#Zadanie 3

def func_3(*args):
    p = 1
    for i in args:
       p*=i
    return p

print(func_3(5,2,7))

#Zadanie 4
str0 = "I study at the University of Warmia and Mazury in Olsztyn"
print(str0[-1::-3])
#Zadanie 5
list0 = ['apple', 'banana', 'pomergranate', 'lime', 'plum', 'orange','melon','cherry','watermelon']
print([x for x in list0 if "l" in x and 'a' in x])

class Frac:
    def __init__ (self,numerator,denominator):
        g = gcd(numerator, denominator)
        self.numerator = numerator//g
        self.denominator = denominator//g


    def __str__(self):
        return str(self.numerator)+'/'+str(self.denominator)


    def __eq__(self,other):
        return (other.numerator, other.denominator) == (self.numerator, self.denominator)

    def __ge__(self,other):
        if other.denominator*self.denominator > 0:
            return self.numerator*other.denominator-other.numerator*self.denominator>=0
        else:
            return self.numerator*other.denominator-other.numerator*self.denominator<=0


    def __add__(self,other):
        return Frac(self.numerator*other.denominator+self.denominator*other.numerator,self.denominator*other.denominator)


    def __sub__(self,other):
        return self + Frac(-other.numerator,other.denominator)



    def __pow__(self,n):
        return Frac(self.numerator **n, self.denominator **n)

    def decimal(self):
        return self.numerator/self.denominator

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

print(Frac(2,10))
print(Frac(2,10)**2)
print(Frac(2,10)==Frac(1,5))
print(Frac(2,10)>=Frac(1,5))
print(Frac(2,5)>=Frac(1,3))
print(Frac(-2,5)>=Frac(-1,3))