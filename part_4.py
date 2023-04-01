import numpy as np

#Array Copy vs. View 
# burada listenin elmanlarını değiştirip yazdırıcaz falan ama ana mevzu şu: view yaptığında np1 ile np2 arasında bir bağ var ve np1 değiştirdiğinde np2 . np2 yi değştirdiğinde np1 değişiyor. Ancak copy de bu bağı tamamen kopartarak işlem yaptığın için np2 kendi başına takılıyor.Aşağıdaki tüm kod kalabalığının ana olayı bu.

np1 = np.array([0,1,2,3,4,5])

# view oluşturayım
np2 = np1.view()

print(f"Orijinal NP1 {np1}")
print(f"Orijinal NP2 {np2}")

np1[0] = 41

print(f"Degistirilmis NP1 {np1}")
print(f"Orijinal NP2 {np2}")

#buranın çıktısı aşağıdaki gibi olur
# Orijinal NP1 [0 1 2 3 4 5]
# Orijinal NP2 [0 1 2 3 4 5]
# Degistirilmis NP1 [41  1  2  3  4  5]
# Orijinal NP2 [41  1  2  3  4  5]

# simdi neden sadece np1 i değiştirmemize ragmen np2 de değişti çünkü onun view i idi mevzu bu.

# --------------------------------------
print('-----------------------------------')


#şimdi de copy i deneyeylim.

np3 = np1.copy()

print(f"Orijinal NP1 {np1}")
print(f"Orijinal NP3 {np3}")

np1[0] = 56

print(f"Degistirilmis NP1 {np1}")
print(f"Orijinal NP3 {np3}")

# burda mesela copy sini aldığımız içün np2 ye miras kalmadı.çıktı şu şekil olacak:
# Orijinal NP1 [41  1  2  3  4  5]
# Orijinal NP3 [41  1  2  3  4  5]
# Degistirilmis NP1 [56  1  2  3  4  5]
# Orijinal NP3 [41  1  2  3  4  5]

# ------------------------------
#garip bir olay şudur ki eğer biz np1 yani orijianl olanı view de iken değiştirmek istemek yerine np2 yi değiştirmek isteseydik bu sefer np1 de değişecekti.A0 Türkçe için kb ama wtf oluyo insan işte.Kodda daha iyi anlatırım.
print('-----------------------------------')

np2 = np1.view()

print(f"Orijinal NP1 {np1}")
print(f"Orijinal NP2 {np2}")

np2[0] = 41

print(f"Degistirilmis NP1 {np1}")
print(f"Orijinal NP2 {np2}")

#çıktı şu şekil
# Orijinal NP1 [56  1  2  3  4  5]
# Orijinal NP2 [56  1  2  3  4  5]
# Degistirilmis NP1 [41  1  2  3  4  5]
# Orijinal NP2 [41  1  2  3  4  5]

# ---------------------------------------
print('-----------------------------------')

np2 = np1.copy()

print(f"Orijinal NP1 {np1}")
print(f"Orijinal NP2 {np2}")

np2[0] = 88

print(f"Degistirilmis NP1 {np1}")
print(f"Orijinal NP2 {np2}")

#çıktı şu şekil
# Orijinal NP1 [41  1  2  3  4  5]
# Orijinal NP2 [41  1  2  3  4  5]
# Degistirilmis NP1 [41  1  2  3  4  5]
# Orijinal NP2 [88  1  2  3  4  5]





 