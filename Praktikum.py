#Tugas Praktikum (Rhendy Diki Nugraha)
data =[]
while True :
    nama = input    ("Nama        : ")
    nim = input    ("NIM         : ")
    tugas = int(input("Nilai Tugas : "))
    uts = int(input("Nilai UTS   : "))
    uas = int(input("Nilai UAS   : "))
    n_akhir = float(tugas)*30/100+(uts)*35/100+(uas)*35/100
    data.append([nama,nim,tugas,uts,uas,n_akhir])

    lanjut= input("Tambah data (y/t)? ")
    if lanjut.lower() =="t":
        break


print("================================================================================================");
print("|  No  |          Nama           |     NIM     |   Tugas   |   UTS   |   UAS   |  Nilai Akhir  |");
print("================================================================================================");
i=0
for x in data:
    i+=1
    print("|  {6:2}  |  {0:20}   |  {1:9}  |  {2:7}  |  {3:5}  | {4:6}  |  {5:11.2f}  |"\
          .format (x[0][:20] , x[1][:9],x[2],x[3],x[4],x[5], i))
print("================================================================================================");