import pandas as pd
#variabel berulang yang menggunakan matriks
list_nim=[]
list_nama=[]
list_uts=[]
list_uas=[]
list_total=[]

Ulang=5
for i in range(Ulang):
     print("data ke - " + str(i+1)) 
     list_nim.append(input("Nim :")) 
     list_nama.append(input("Nama :")) 
     list_uts.append(input("Uts :")) 
     list_uas.append(input("Uas :")) 
#proses
for i in range(Ulang):
     list_total.append((list_uas[i] + list_uts[i] /2)) 

tamu = {
      "Nim" : list_nim, 
      "Nama Lengkap" : list_nama, 
      "Nilai UTS" : list_uts, 
      "Nilai UAS" : list_uas,
      "Rata-rata" : list_total
}
data_tamu = pd.DataFrame(tamu) 
#cetak
print("--------------- Daftar Nilai ------------") 
print(data_tamu) 
print("-----------------------------------------")