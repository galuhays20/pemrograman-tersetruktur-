def Ha (b,c):
    return((c*c)-(b*b)== a)
def Hb (a,c):
    return((c*c)-(a*a)== b)
def Hc (a,b):
    return((a*a)+(b*b)== c)
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))

if (b,c==Ha) and (a,c==Hb) and (a,b==Hc):
    print('-> True')
else:
    print('-> False')
