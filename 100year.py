'''
Buat program yang meminta user untuk memasukkan (input) nama dan usia mereka. Cetak pesan
sapaan untuk mereka (plus nama user) dan tahun berapa mereka akan berusia 100 tahun.
'''

import datetime # Modul untuk mendapat tahun saat ini

name = input('Siapa namamu?') #Meminta user untuk memasukkan namanya
usia = int(input('Berapa usiamu saat ini?')) #Meminta user untuk memasukan usianya saat ini convert menjadi integer
tahun_sekarang = datetime.date.today().year #Mendapatkan tahun saat ini
tahunusia100 = tahun_sekarang-usia+100 #Menghitung tahun saat usia user 100 tahun
print("Halo", name) #Menyapa user
print('Kamu akan berusia 100 tahun di tahun',tahunusia100) #Memberi tahu kapan user berusia 100 tahun
