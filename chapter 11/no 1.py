from datetime import *
def diffDate(x):
    tglskrg = datetime.now()
    a = str(tglskrg.year)+'-'+str(tglskrg.month)+'-'+str(tglskrg.day)
    tgl = datetime.strptime( a, '%Y-%m-%d')
    date = datetime.strptime( x, '%Y-%m-%d')
    y = date - tgl
    print(y.days)
    return y.days

diffDate('2021-12-15')
