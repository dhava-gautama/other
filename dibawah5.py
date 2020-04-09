'''
Buat sebuah list: [2, 3, 5, 7, 8, 11, 11, 3, 5, 6, 0.3, 0.44, 20, 100]. Gunakan program Python untuk
hanya memunculkan angka-angka di dalam list yang nilainya kurang dari atau sama dengan 5.
'''

data = [2, 3, 5, 7, 8, 11, 11, 3, 5, 6, 0.3, 0.44, 20, 100] #Membuat array
for i in range(0,len(data)): #Looping
    if data[i] <=5: #Bila nilai ke-1 pada array data kurang dari 5 maka
        print (data[i]) #Print nilai
