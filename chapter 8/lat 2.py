def dataStat(x):
    maks = max(x)
    minimum = min(x)
    average = sum(x)/ len(x)

    return [round(average), maks, minimum]

data = [8,9,10,11]
print('cari [Rata-rata, Max, Min]dari', data)
print('adalah', dataStat(data))

