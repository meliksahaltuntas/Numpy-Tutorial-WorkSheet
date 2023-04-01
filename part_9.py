import numpy as np
# Filtering Numpy Arrays With Boolean Index Lists
np1 = np.array([1,2,3,4,5,6,7,8,9,10])

x = [True,True,False,False,False,False,False,False,False,False]

print(np1) # çıktı: [ 1  2  3  4  5  6  7  8  9 10]
print(np1[x]) # çıktı:  [1 2]  yani sadece True olanları bastırdı.

# bu baya yavaş bir yöntem olduğu için farklı şeyler düşünmemiz lazım. Bunun için for döngülü falan bir şeyler yazalım bakalım ne olacak.

filtered = []  #sıradan çinko python list objesi yani magic burda değil.

for thing in np1:
    if thing % 2 == 0:
        filtered.append(True)
    else:
        filtered.append(False)

print(np1) #çıktı: [ 1  2  3  4  5  6  7  8  9 10]
print(filtered) #çıktı:  [False, True, False, True, False, True, False, True, False, True]
print(np1[filtered]) #çıktı: [ 2  4  6  8 10]

#gördüğün gibi çok daha kolay ve hızlı oldu böylece milyon tane veriyi bile filtreleyebilirsin.

print('------------------------------')
# aynı cevapları numpy ın kısaltılmış syntax ı ile daha farklı şekilde alabiliriz.Örnek:
filter = np1 % 2 == 0
print(np1)
print(filtered)
print(np1[filtered])


# Bu kadardı Allah'a emanet olun. 
# Meliksah Altuntas
# Made by <3 in Istanbul 2023 March 

