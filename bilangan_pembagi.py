print('Program pencari pembagi angka')
number = int(input('Masukan angka'))
print('Pembagi bilangan tersebut adalah')
for i in range(1,number):
    if number%i == 0:
        print(i)
