def starFormation1(n):
    for i in range(1, n+1):
        for j in range(i):
            print('*', end='')
        print('')
starFormation1(4)
print('')

