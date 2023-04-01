import numpy as np

# normal bir python listesi böyledir 

list1 = [1,2,3,4,5]
print(list1)


# hatta python değişik çeşitteki datalari birlikte ayni array içinde tutmamiza izin verir mesela:

list2=["Meliksah Altuntas",21,[1,2,3,4,5],True]
print(list2)

# ancak maalesef çok çok büyük devasa verilerle uğraşırken bu veri karmaşası dezavantaj oluyor. Numpy tam da burada devreye giriyor.

# Btw numpy ın açılımı Numeric Python yani o kadar da farklı bi şey değil :)

# ndarray = n-dimensioanal array

np1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(np1)
print(np1.shape) #eleman sayısını verir

np2 = np.arange(10) # bu normal range 
print(np2)

np3 = np.arange(0,10,2) # 0 dan 10 uncu iteme kadar 2 şer atlayarak gider.

np4 = np.zeros(10) #belirttingin range e kadar 0 yapar
print(np4)

np5 = np.zeros((2,10)) # bu da multidimensional şeqli
print(np5)

np6 = np.full((10),6) # 10 kutuyu da 6 ile doldurur.
print(np6)

np7 = np.full((2,10),6) # 2 sütunluk 10 satırı da 6 ile doldurur. yani multidimensional iste.
print(np7)

# --------------------------------
# python listesini np listesine çevir

my_list = [1,2,3,4,5]
np8 = np.array(my_list)
print(np8)

