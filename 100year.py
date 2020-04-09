import datetime

name = input('Siapa namamu?')
usia = int(input('Berapa usiamu saat ini?'))
tahun_sekarang = datetime.date.today().year
tahunusia100 = tahun_sekarang-usia+100
print("Halo", name)
print('Kamu akan berusia 100 tahun di tahun',tahunusia100)
