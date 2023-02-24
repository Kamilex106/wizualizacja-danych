import math
x = 5.5
y = 5.7
a = 10
b = 25
# print(math.ceil(x))
# print(math.floor(x))
# print(round(x))
# print(x.is_integer())
# print(isinstance(a,int))
def funkcja1(x,y):
    if isinstance(x,int)==True and isinstance(y,int)==True:
        print(x%y)

    elif isinstance(x,float) == True or isinstance(y,float) == True:
        print(math.fmod(x,y))
def funkcja2(a,n):
    for k in range(1,n+1):
        print(k)
        print(math.log(k,a),"|")
def funkcja2b(a,n):
    logs = [str(math.log(a,k)) for k in range(1,n+1)]
    print('|'.join(logs))

def funkcja3(a):
    print(math.exp(a))
    print(math.e**a)
    print(math.pow(math.e, a))



##print(funkcja1(x,y))
##print(funkcja2(a,b))
print(funkcja3(a))