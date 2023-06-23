nama=[]
email=[]
n_wa=[]
alamat=[]
m_plh=[]
j_py=[]
jml=[]
m_bayar=[]
total=[]
harga=[]
ulang=2
for i in range(ulang):
    print("Pesanan ke-" + str(i+1))
    nama.append(input("Masukkan nama Anda          : "))
    email.append(input("Masukkan E-mail Anda         : "))
    n_wa.append(input("Masukkan Nomor WA Anda       : "))
    alamat.append(input("Masukkan Alamat Anda         : "))
    m_plh.append(input("Masukkan versi yang dipilih       : "))
    j_py.append(input("Jenis Payment yang dipilih[pba/jca]  : "))
    jml.append(input("Masukkan Jumlah album        : "))
    m_bayar.append(input("Masukkan metode pembayaran [EWT/TFB]     : "))
    
    if j_py[i] == "pba" :
        detail = "Full payment"
        versi ="Photo book"
        harga.append(jml*285000) 
    elif j_py == "jca":
        detail= "Full payment"
        versi = "Jewel case"
        harga.append(jml*185000)
    else :
        print("Kode yang Anda masukkan salah silahkan input ulang :)")
        print("pba[Photobook;Full payment]/jca[Jewel case;Full payment]")
        
        if m_bayar == "EWT" :
            D_metode = "E-Wallet [Dana&Spay] 083816716161 a/n Buna" 
        elif m_bayar == "TFB" :
             D_metode = "Transfer Bank [BCA] 3300023060 a/n Buna"
        else :
            print("\n =================================================================== \n")
            print("Kode Metode Pembayaran yang Anda masukkan salah,silahkan coba lagi :)\n")
            print("Kode Metode Pembayaran : EWT(E-Wallet[Dana/Spay])/TFB(TF Bank [BCA])")

    
    

for i in range(ulang):
    print("\n ==================================================================")
    print("| >.<Pemesanan 3rd Album UNIVERSE NCT 2021 [Jewel Case Version]>.< |")
    print(" ==================================================================")
    print(" Nama Pemesan        : ", nama=[i] )
    print(" E-mail Pemesan      : ", email=[i] )
    print(" Nomor WA            : ", n_wa=[i] )
    print(" Alamat              : ", alamat=[i] )
    print(" Jenis Payment       : " , j_py=[i])
    print(" Album Version       : " , m_plh=[i])
    print(" Jumlah Album        : " , jml=[i])
    total.append(int(jml*harga))
    print(" Jumlah yang dibayar :  Rp." ) 
    print(" Metode Pembayaran   : ", m_bayar=[i])
    print("\n =================================================================\n")
    print("                   TERIMAKASIH ATAS PESANANNYA !!!                    ")            
    print("\n =================================================================\n")



