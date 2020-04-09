'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]. 
Buat program python untuk mencari elemen-elemen yang ada di list a dan list b tanpa pengulangan.
'''

import numpy # Mengimport modul numpy

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] #Array ke-1
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] #Array ke-2
c = numpy.intersect1d(a,b) #Mencari elemen sama yang berada pada array a dan array b

print(c) #Print element array yang sama
