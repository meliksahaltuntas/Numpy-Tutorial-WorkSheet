import numpy as np
#Searching Numpy Arrays 

np1 = np.array([1,2,3,4,5,6,7,8,9,10,3])

x = np.where(np1 == 3) #kaçıncı indexte olduğunu verir.
print(np1)
print(x) #çıktı: (array([2, 10], dtype=int64),)
print(x[0]) #çıktı:[2 10]
print(np1[x[0]]) #çıktı: [3 3] kaç tane 3 varsa onun adeti kadar 3 basar.

# çift indexli sayıları yazdır
y = np.where(np1 % 2 == 0)
print(y[0]) #çıktı:[1 3 5 7 9] index sıfırdan başladığı için indexte çift sayıları saymada tek sayıları yazdırdı.


# tek indexli sayıları yazdır
z = np.where(np1 % 2 == 1)
print(z[0]) #çıktı:[ 0  2  4  6  8 10] index sıfırdan başladığı için indexte tek sayıları, saymada çift sayıları yazdırdı.

