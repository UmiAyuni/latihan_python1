def Persegi(p,l):
    print("Menghitung Luas Persegi Panjang")
    p=int(input("Masukkan Panjang: "))
    l=int(input("Masukkan Luas: "))
    luas=p*l
    print("Luas persegi panjang adalah : ",luas)
    lagi=input("Mau input lagi?")
    if(lagi=="Y"):
        pilihan()
    elif(lagi=="N"):
        print("Terimakasih")

def Lingkaran(r):
    print("Menghitung Luas Lingkaran")
    r=int(input("Masukkan Jari-jari : "))
    luas=float(3.14*r*r)
    print("Luas Lingkaran adalah : ",luas)
    lagi=input("Mau input lagi?")
    if(lagi=="Y"):
        pilihan()
    elif(lagi=="N"):
        print("Terimakasih")

def Segitiga(a,t):
    print("Menghitung Luas Segitiga")
    a=int(input("Masukkkan Alas Segitiga: "))
    t=int(input("Masukkan Tinggi Segitiga: "))
    luas=(a*t)/2
    print("Luas Segitiga Adalah : ",luas)
    lagi=input("Mau input lagi? ")
    if(lagi=="Y"):
        pilihan()
    elif(lagi=="N"):
        print("Terimakasih")

def pilihan():
    print("\n Selamat Datang di Program untuk Menghitung Luas")
    print("-----------------------------------------------\n")
    print("Menu Pilihan \n 1. Persegi Panjang \n 2. Lingkaran \n 3. Segitiga \n 4. Keluar  ")
    pilihAngka()

def pilihAngka():
    p=0
    l=0
    r=0
    a=0
    t=0
    i=int(input("Masukkan Pilihan Angka[1,2,3]: "))
    if(i==1):
        Persegi(p,l)
    elif(i==2):
        Lingkaran(r)
    elif(i==3):
        Segitiga(a,t)
    elif(i==4):
        print("Terimakasih")
    else:
        pilihan()

pilihan()
