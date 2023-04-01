import numpy as np

#Sorting Numoy Arrays / Sıralama

np1 = np.array([6,7,8,9,0,2,1])

print(np1) #olduğu gibi yazdırır
print(np.sort(np1)) # küçükten büyüğe

np2 = np.array(['Meliksah','Satık','Emre','Melih','Abdullah'])

print(np2) #olduğu sıralamada yazar
print(np.sort(np2)) #alfabetik yazar


np3 = np.array([True,False,True,False])
print(np3) #olduğu sıralamada yazar
print(np.sort(np3)) #False lar 0 sıfır değerini taşıdığı için onları daha öncelendirip sıralayarak yazdırır.


#sort ettiğin bir array sortlandığında orijinal arrayde bir değişim olmaz çünkü copy si alınır.Aşağıya örnek yazdım.
print(np1) #olduğu gibi yazdırır
print(np.sort(np1)) # küçükten büyüğe
print(np1) #orijinal np1 değişmeden yazdırılır.



#2-D sıralama / çok boyutlu arraylerde sort kullanınca sadece kendi satırında sıralanır.Yani her satır kendi içinde çalışır.
np4 = np.array([[7,6,2,9],[8,3,5,0]])
print(np4)
print(np.sort(np4))