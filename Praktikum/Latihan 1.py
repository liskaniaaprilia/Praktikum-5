# Latihan 1

print("Nama : Liskaniaa Aprilia, 312210383")
print("latihan membuat sebuah list sebanyak 5 elemen dengan nilai bebas")
print("==============================================================")

print('membuat 5 bilangan secara acak')
t = [1, 2, 3, 4, 5]
print(t) # untuk menampilkan semua element
print(t[2]) # untuk menampilkan element ke 3
print(t[1:3]) # untuk menampilkan element ke 2 dan ke 4
print(t[4]) # untuk menampilkan element terakhir

print("==============================================================")

print('ubah element list')
t[3] = 27 # untuk mnegubah element ke 4
print(t[3]) # untuk menampilkan elemen ke 4 yang sudah diganti nilainya
t[3:4] = 27, 7 # untuk mengubah element ke 4 sampai akhir
print(t[3:5]) # untuk menampilkan element ke 4 dan 5 yang sudah diganti nilainya

print("==============================================================")

print('tambah element list')
s = t[0:2] # untuk menggabung element 1 dan 2
print(s)
s.append(45) # untuk menambah list dari element 1 dan 2
print(s)
s.extend([6, 7, 8]) # untuk menambahkan 3 buah nilai pada list
print(s)
r = t + s # untuk menggabungkan hasil semua list
print(r)

print("==============================================================")














