import numpy as np

# slicing arrays yani gavurcadan mealen listeleri ayırma metodları bu bölümde işlenecek.

np1 = np.array([1,2,3,4,5,6,7,8,9])

print(np1[1:5]) #birinci itemden beşinci iteme kadar yazdırır 1 dahil ama 5 değil yani 2 3 4 5 yazdır 5. indexteki 6 yazdırılmıyor.


print(np1[3:]) # iki noktadan sonrasını boş bırakmak demek dibine sonu kadar yazdır demek yani 4 5 6 7 8 9

print(np1[-3:-1]) #bu da negatiften terse yazdırır yani sonuncusunu yazdırmaz yani 7 8

print(np1[1:5:2]) #bu da adım adım atlamalı yazdırır.yani 1 den 5 e kadar ikişer ikişer yani 2 4

print(np1[::2]) #sadece ikişer ikişer atlayarak tüm listeyi yazdırır.yani 1 3 5 7 9

# ----------------------------
np2 = np.array([
                [1,2,3,4,5]
               ,[6,7,8,9,10]
               ]) # iki dimensionallı array 

print(np2[1,2]) #burada 2.satırdaki(index numarası 1) ve 3.sütundaki(index numarası 2) numaryı yazdıracak yani 8

print(np2[0:1,1:3]) #burası biraz karışık ama anlarsan iyi olur simdi ilk element yani 0:1 hangi satırdan hangi satıra kadar bakacagını gösteriyor yani burada indexi 0 dan, indexi 1 olana kadar ama 1 dahil değil yani sadece ilk satıra bak diyor. ikinici element ise o satırdaki hangi sütunları alman gerektiğini belirliyor burda ben 1:3 yaptım 1 den başlar 1 dahil ama 3 dahil değil yani 2 3


print(np2[0:2,1:3]) #burda da 0 dan 2 ye kadar satırlara bak ama 2 dahil değil ondan sonra da 1 ve 3 üncü sütunlarındaki sayıları yazdır yani
                                            # [[2 3]
                                            #  [7 8]]



