'''
Buat program yang meminta user memasukkan sebuah angka. Jika angkanya ganjil, tuliskan “Anda
memasukkan angka ganjil”. Jika angkanya genap, tuliskan “Anda memasukkan angka genap”.
'''

print("Angkamu ganjil atau genap yaa.. Yuk kita check")
number = int(input('Masukan angka yang ingin anda check')) #Meminta user untuk memasukan angka
if number%2 == 0: # Bila sisa bagi angka/2 = 0 maka bilangan tersebut genap
    print('Angkamu genap')
else: # Bila tidak bilangan tersebut ganjil
    print('Angkamu ganjil')
