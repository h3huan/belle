def grop(x):
    if x==0:
        return 0
    else:
        return float(1/x)
def printa(x):
   print('f(',x,') = ',round(grop(6),1))

# y= input()
# printa(y)

def elec(x):
    if x<=50:
        return x*0.53
    elif x>50:
        return 50*0.53 + (x*50)*0.58

def price(x):
    if x<0:
        print('卷铺盖滚蛋')
    else:
        print('cost =', elec(x))

# y = float(input('没来交电费的户啊'))
# price(y)

def multi(x,n):
    i = 0
    z = 0
    while i<n:
        z += x*(10**i)
        i += 1
    return z
def multiplus(x,n):
    i = 1
    z = 0
    while i < n+1:
        z += multi(x,i)
        i += 1
    print(z)

# multiplus(4,4)
def hulam(x):
    return float(x/(2*x-1))*((-1)**(x-1))
def mu(x):
    i = 1
    z = 0
    while i<x+1:
        z += hulam(i)
        i += 1
    print(round(z,3))
mu(2)