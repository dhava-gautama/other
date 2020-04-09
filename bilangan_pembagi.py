'''
Buat program yang meminta user untuk memasukkan (input) sebuah angka. Cetak semua pembagi
dari angka tersebut, disini pembagi adalah bilangan yang membagi habis bilangan yang diinput user.
Contoh: 6 pembaginya adalah 6, 3, 2, dan 1.
'''

print('Program pencari pembagi angka')
number = int(input('Masukan angka')) #Meminta user untuk menginput angka yang akan dicari pembaginya
print('Pembagi bilangan tersebut adalah')
for i in range(1,number+1): #Untuk angka range 1-number
    if number%i == 0: #Bila sisa bagi = 0 maka bilangan tersebut adalah bilangan pembagi
        print(i) #Print bilangan pembagi
