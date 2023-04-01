np2 = np1.view()

# print(f"Orijinal NP1 {np1}")
# print(f"Orijinal NP2 {np2}")

# np1[0] = 41

# print(f"Degistirilmis NP1 {np1}")
# print(f"Orijinal NP2 {np2}")

# #buranın çıktısı aşağıdaki gibi olur
# # Orijinal NP1 [0 1 2 3 4 5]
# # Orijinal NP2 [0 1 2 3 4 5]
# # Degistirilmis NP1 [41  1  2  3  4  5]
# # Orijinal NP2 [41  1  2  3  4  5]

# # simdi neden sadece np1 i değiştirmemize ragmen np2 de değişti çünkü onun view i idi mevzu bu.

# # --------------------------------------
# print('-----------------------------------')


# #şimdi de copy i deneyeylim.

# np3 = np1.copy()

# print(f"Orijinal NP1 {np1}")
# print(f"Orijinal NP3 {np3}")

# np1[0] = 56

# print(f"Degistirilmis NP1 {np1}")
# print(f"Orijinal NP3 {np3}")