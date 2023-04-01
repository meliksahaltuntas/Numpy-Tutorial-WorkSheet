import numpy as np

#shape and reshape numpy arrays

#bazen yatmadan önce başınızı yastığa koyduğunuzda aklınıza bir soru gelir. Ya ben 3 dimensioanl'lı bir matrisin tek veya iki dimensional'a nasıl çekebilirim. İşte bu bölümde çok boyutlu matrislerin boyutlarıyla oynayacağız.Sırf siz rahat uyuyun diye.

np1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12]) # hemen 1-D bir array oluşturdum.
print(np1)
print(np1.shape)

print("---------------------------------")

np2 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]]) # 2-D bir array oluşturdum.
print(np2)
# [[ 1  2  3  4  5  6]
#  [ 7  8  9 10 11 12]]

print(np2.shape) #(2, 6) burada 2 satır sayısını, 6 sütun sayısını gösterir.

print("---------------------------------")

#reshape 2-D
np3 = np1.reshape(3,4) #meali: np1 i 3 satır 4 sütunlu hale getir. zaten 12 elemanlı ya

print(np3)
#çıktı
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

print("---------------------------------")

np4 = np1.reshape(2,3,2)
print(np4)
#çıktı
# [[[ 1  2]
#   [ 3  4]
#   [ 5  6]]

#  [[ 7  8]
#   [ 9 10]
#   [11 12]]]


print("---------------------------------")
#flatten to 1-D / çok boyutlu bir matrisi tek boyutta 'düzleştirme'

np5 = np4.reshape(-1)
print(np5) # çıktı: [ 1  2  3  4  5  6  7  8  9 10 11 12]