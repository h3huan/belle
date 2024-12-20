def qiu_he(a,n):
    t = 0
    for e in range(0,n):
        d = 0
        for i in range(0,e+1):
            d += a * 10**i
        t += d
        print(d)
    return t

def countdigit(num, dit):

    la = list(map(int, str(num)))
    a=0
    for i in range(0,len(str(num))):
        if la[i] == dit:
            a += 1
    return a

