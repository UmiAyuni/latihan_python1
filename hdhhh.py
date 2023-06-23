jml_karyawan=input("Jumlah Karyawan: ")
bln=input("Bulan: ")
print("Input Data Karyawan")
dt_karyawan=input("Data Karyawan ke: ")
nip=input("NIP Karyawan: ")
nama=input("Nama Karywan: ")
kd_jabatan=input("Kode Jabatan [1/2]: ")
kd_status=input("Kode Status [M/S]: ")

if kd_jabatan=="1":
    nama_jabatan= "Administrasi"
    gaji_pokok=800000
    if kd_status=="M":
       nama_status="Menikah"
       tunjangan=200000
    elif kd_status=="S":
        nama_status="Single"
        tunjangan=100000
elif kd_jabatan=="2":
    nama_jabatan= "Operasional"
    gaji_pokok=850000
    if kd_status=="M":
       nama_status="Menikah"
       tunjangan=250000
    elif kd_status=="S":
        nama_status="Single"
        tunjangan=150000

total_gaji=int(gaji_pokok+tunjangan)


print("               Daftar Gaji Karyawan            ")
print("              'PT YUVERTY SEJAHTERA'           ")
print("Bulan=  ",bln           )
print("=============================================================================")
print("No           NIP Karyawan     Nama Karyawan    Jabatan            Gaji total ")
print(dt_karyawan,  nip,             nama,            nama_jabatan,     total_gaji   )