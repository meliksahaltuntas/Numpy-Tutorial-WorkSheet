import numpy as np

#Iterating Through Numpy Arrays

np1 = np.array([1,2,3,4,4,5,6,7,8,9,10]) # 1_D array

for x in np1:
    print(x)


print('-------------------------')

np2 = np.array([[1,2,3,4,5],[6,7,8,9,10]]) # 2-D array

for x in np2:
    print(x)
#çıktı
# [1 2 3 4 5]
# [ 6  7  8  9 10]

for x in np2: # normal 1-D gibi yazdırır.
    for y in x:
        print(y) 


print('-------------------------')

# 3-D array
np3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) 

for x in np3:
    print(np3)

for x in np3:
    for y in x:
        print(y)

for x in np3:
    for y in x:
        for z in y:
            print(z)

#her iç for dögüsü bir boyut azaltır. en yukarıdaki 3D ortadaki 2D ve en alttaki ise 1D. Its cool isnt it ?!?!


#listeyi kaç boyutlu olursa olsun en basic level yazdırılabileceği şekilde yazdıran bir fonksiyon da var adı 'nditer' aşağıda bi örnek yapıp geçicem.

for x in np.nditer(np3):
    print(x)
    

