'''
Buat sebuah game. Tentukan nomor acak antara 1-9. Minta user menebak sebuah angka.
Jika angka yang disebutkan user lebih kecil daripada angka acak, katakan “Angka yang kamu masukkan terlalu kecil.”.
Jika angka yang disebutkan user lebih dari angka acak, katakan “Angkanya kegedean.”.
Jika user menebak dengan benar, katakan “Selamat, Angka yang anda tebak benar!”
'''

import random
number = random.randrange(1,10) # Membuat angka random antara 1-9
print(number)
print('Main tebak-tebakan yuk.')
print('Aku punya angka diantara 1-9. Coba kamu tebak angka berapa itu. Kamu punya 3 kesempatan')
for i in range(0,3): #Memberi 3 kesempatan
    tebakan = int(input("Tebakanku adalah")) #Meminta user untuk memasukan tebakan
    if tebakan < number: # Bila nilai tebakan kurang dari number
        print("Angka yang kamu masukkan terlalu kecil.")
    elif tebakan > number: # Bila nilai tebakan lebih dari number
        print("Angkanya kegedean.")
    elif tebakan == number:# Bila nilai tebakan sama dengan number
        print("Selamat, Angka yang anda tebak benar!")
