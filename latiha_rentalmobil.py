#input
NIK_Penyewa=input("Masukan NIK Penyewa Mobil    : ")
nama_penyewa=input("Masukan Nama Penyewa   : ")
kode_mobil=input("Masukan Kode Mobil    : ")
#proses
if kode_mobil=="XNA":
    namamobil="Xenia"
    harga=60000
elif kode_mobil=="AVZ":
    namamobil="Avanza"
    harga=65000
else :
    kode_mobil=="CLY"
    namamobil="Calya"
    harga=55000

#Input jam sewa
jam_sewa=int(input("Jumlah Jam Sewa     : "))

biaya_sewa=int(jam_sewa*harga)

#cetak hasil
print("---------------------------------------------------")
print("               RENTAL MOBIL ZIAN TRANS             ")
print("---------------------------------------------------")
print("NIK Penyewa  : " +str(NIK_Penyewa))
print("Nama Penyewa : " +str(nama_penyewa))
print("Kode Mobil   : " +str(kode_mobil))
print("Nama Mobil   : " +str(namamobil))
print("---------------------------------------------------")
print("Jumlah Jam Sewa      : " ,jam_sewa)
print("Harga Sewa Perjam    :Rp." ,harga)
print("Biaya Sewa           :Rp." ,biaya_sewa)