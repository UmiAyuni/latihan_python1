def Pilihan():
    print('''
    ============================================================
                   Penyewaan Baju Adat Tradisional         
                         Kanza Collection                       
    +==========================================================+
    |Kode Paket  |       Nama Baju Adat       |       Harga    |
    |------------|----------------------------|----------------|
    |    JT      |         Jawa Timur         |  Rp.200.000,00 |
    |    JB      |         Jawa Barat         |  Rp.250.000,00 |
    |    SB      |       Sumatera Barat       |  Rp.300.000,00 |
    +==========================================================+

    \n ''')
    data ()

def data ():
    nama=input("Masukan Nama Penyewa    : ")
    no_hp=input("Masukan No Handphone Penyewa   : ")
    kode_paket=input("Masukan Kode Paket [JT/JB/SB]   : ")
    u_pakaian=input("Masukan Ukuran Pakaian [M/L/XL]   : ")
#proses
    if kode_paket=="JT":
        namabaju="Jawa Timur"
        harga=200000
    elif kode_paket=="JB":
        namabaju="Jawa Barat"
        harga=250000
    elif kode_paket=="SB":
        namabaju="Sumatera Barat"
        harga=300000
    else :
        namabaju="Tidak Ada"
        harga=0

#Input lama sewa
    l_sewa=int(input("Masukan Lama Sewa   : "))

    biaya_sewa=int(l_sewa*harga)

#cetak hasil
    if kode_paket == 'JT' or kode_paket == 'JB' or kode_paket == 'SB':
        print("\n====================================================\n")
        print("        Penyewaan Baju Adat Tradisional         ")         
        print("                 Kanza Collection               ")
        print("\n===================================================\n")
        print("Selamat Datang di Butik Kami !                       \n")
        print("Nama Penyewa     : " +str(nama))
        print("No HP Penyewa    : " +str(no_hp))
        print("Kode Paket Adat  : " +str(kode_paket))
        print("Nama Baju Adat   : " +str(namabaju))
        print("Ukuran Baju      : " +str(u_pakaian))
        print("-----------------------------------------------------\n")
        print("Lama Sewa           : " , l_sewa, "/hari")
        print("Harga Sewa          :Rp." ,harga)
        print("Total biaya sewa    :Rp." ,biaya_sewa)
        print("\n====================================================\n")
        ulang=str(input("Apakah Anda ingin menyewa lagi? [Y/y] : "))
        ulang = "Y"
        while ulang == "Y" or ulang == "y":
            Pilihan()

Pilihan()