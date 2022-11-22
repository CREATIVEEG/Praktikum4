#Latihan List ( Rhendy Diki Nugraha )

#Membuat sebuah list sebanyak 5 elemen dengan nilai bebas
a = [1, 4, 6, 8, 9]
print("List A =", a,)
# *Akses List
print("Elemen ke 3 adalah       :", a[2]) #Menampikan elemen 3
print("Elemen ke 2 - 4 adalah   :", a[1:4]) #Menampilkan elemen 2-4
print("Elemen terakhir adalah   :", a[4]) #Menampilkan elemen terakhir

# *Ubah Elemen List
a[3] = 7
print("Elemen 4 > 7             :", a) #Mengubah elemen 4
a[3:5] = [7, 10]
print("Elemen 4-5 > 7, 10       :", a,"\n") #Mengubah elemen 4-5

# *Tambah Elemen List
a = [1, 4, 6, 8, 9]
b = [3, 7, 10, 11, 20]
print("List A =", a)
print("List B =", b)

b.extend(a[1:3])
print("Ambil 2 elemen A jadi List B     :",b) #Mengambil 2 bagian A jadi B

b = [3, 7, 10, 11, 20]
b.append("14")
print("Tambah nilai string ke list B    :",b) #Menambah list B dengan nilai string

b = [3, 7, 10, 11, 20]
b.extend([25, 28, 30])
print("Menambah 3 nilai ke list B       :",b) #Menambah list B dengan 3 nilai

b = [3, 7, 10, 11, 20]
b = b + a
print("Menggabung List B dengan A       :",b) #Menggabungkan list B dan A