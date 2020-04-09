'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]. 
Buat program python untuk mencari elemen-elemen yang ada di list a dan list b tanpa pengulangan.
'''

data = [2, 3, 5, 7, 8, 11, 11, 3, 5, 6, 0.3, 0.44, 20, 100] #Membuat array
for i in range(0,len(data)): #Looping
    if data[i] <=5: #Bila nilai ke-1 pada array data kurang dari 5 maka
        print (data[i]) #Print nilai
