#Praktikum 1

#nomor 2
bil=10
if(bil>0):
    print("Bilangan positif")

print()

#nomor empat
bil=-4
if(bil>0):
    print("Bilangan positif")
else :
    print("Bilangan negatif atau nol")

print()

#nomor enam
bil=0
if(bil>0):
    print("Bilangan positif")
elif(bil<0):
    print("Bilangan negatif")
else:
    print("Bilangan nol")

print()

#nomor delapan
a=-2
b=-7
if(a>0)and(b>0):
    print("Keduanya positif")
elif(a>0)or(b>0):
    print("Salah satunya positif")
elif(a<0)or(b<0):
    print("Salah satunya negatif")
elif(a<0)and(b<0):
    print("Keduanya negatif")

print()

#nomor sepuluh
a=-2
b=-7
if(a<0)or(b<0):
    print("Salah satunya negatif")
elif(a>0)and(b>0):
    print("Keduanya positif")
elif(a>0)or(b>0):
    print("Salah satunya positif")
elif(a<0)and(b<0):
    print("Keduanya negatif")

print()

#nomor sebelas
a=-2
b=-7
if(a>0)and(b>0):
    print("Keduanya positif")
if(a>0)or(b>0):
    print("Salah satunya positif")
if(a<0)or(b<0):
    print("Salah satunya negatif")
if(a<0)and(b<0):
    print("Keduanya negatif")

print()

#nomor duabelas
a=8
b=3
if(a>0)and(b>0):
    print("Keduanya positif")
else:
    print("Keduanya tidak positif")

a=8
b=3
if(a>0):
    if(b>0):
        print("Keduanya positif")
    else:
        print("Keduanya tidak positif")
else:
    print("Keduanya tidak positif")

print()

#nomor tigabelas
a=-8
b=3
if(a>0)and(b>0):
    print("Keduanya positif")
else:
    print("Keduanya tidak positif")

a=8
b=-3
if(a>0):
    if(b>0):
        print("Keduanya positif")
    else:
        print("Keduanya tidak positif")
else:
    print("Keduanya tidak positif")

print()

#Latihan

#nomor satu
print("Status Kelulusan Siswa")
NilaiBhsIndo=a=int(input("Masukkan nilai bahasa indonesia:"))
NilaiIPA=b=int(input("Masukkan nilai IPA:"))
NilaiMatematika=c=int(input("Masukkan nilai matematika:"))

if(a>60):
    if(b>60):
        if(c>70):
            print("LULUS")
else:
    print("TIDAK LULUS")

print()

#nomor dua
print("Status Kelulusan Siswa")
NilaiBhsIndo=a=int(input("Masukkan nilai bahasa indonesia:"))
NilaiIPA=b=int(input("Masukkan nilai IPA:"))
NilaiMatematika=c=int(input("Masukkan nilai matematika:"))
if(a>0)and(a<100):
    if(b>0)and(b<100):
        if(c>0)and(c<100):
            print("LULUS")
else:
    print("Maaf input ada yang tidak valid")

print()

#nomor tiga
print("Status Kelulusan Siswa")
a=Nilaibahasaindonesia=int(input("Masukkan nilai bahasa indonesia:"))
b=NilaiIPA=int(input("Masukkan nilai IPA:"))
c=Nilaimatematika=int(input("Masukkan nilai matematika:"))

if(a>60):
    if(b>60):
        if(c>70):
            print("LULUS")
else:
    print("TIDAK LULUS")

print("Sebab:")
if(a<60)and(b>60)and(c>70):
    print("Nilai bahasa indonesia kurang dari 60")
if(a>60)and(b<60)and(c>70):
    print("Nilai IPA kurang dari 60")
if(a>60)and(b>60)and(c<70):
    print("Nilai matematika kurang dari 70")

print()

#nomor empat
kode=input("Masukkan kode karyawan:")
nama=input("Masukkan nama karyawan:")
golongan=input("Masukkan golongan:")

if(golongan=="A"):
    gajiPokok=10000000
    potongan=2.5
    gajiKotor=10000000+0
    jumlahPotongan=2.5/100*gajiKotor
    gajiBersih=gajiKotor-jumlahPotongan
elif(golongan=="B"):
    gajiPokok=8500000
    potongan=2.0
    gajiKotor=8500000+0
    jumlahPotongan=2.0/100*gajiKotor
    gajiBersih=gajiKotor-jumlahPotongan
elif(golongan=="C"):
    gajiPokok=7000000
    potongan=1.5
    gajiKotor=7000000+0
    jumlahPotongan=1.5/100*gajiKotor
    gajiBersih=gajiKotor-jumlahPotongan
elif(golongan=="D"):
    gajiPokok=5500000
    potongan=1.0
    gajiKotor=5500000+0
    jumlahPotongan=1.0/100*gajiKotor
    gajiBersih=gajiKotor-jumlahPotongan
    

print("======================================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("------------------------------------------------------")
print("Nama Karyawan         :",nama)
print("Golongan              :",golongan,"Kode:",kode)
print("------------------------------------------------------")
print("Gaji Pokok            :",gajiPokok)
print("Potongan              :",jumlahPotongan)
print("---------------------------------------------------- -")
print("Gaji Bersih           :",gajiBersih)

print()

#nomor lima
kode=input("Masukkan kode karyawan:")
nama=input("Masukkan nama karyawan:")
golongan=input("Masukkan golongan:")
status=input("Masukkan status(1:Menikah, 2:Belum):")

if(status=="1"):
    jumlahAnak=int(input("Masukkan Jumlah Anak:"))
    tunjanganSuamiIstri=10/100
    tunjanganAnak=5/100*jumlahAnak
    status="Sudah Menikah"
else:
    jumlahAnak=0
    tunjanganSuamiIstri=0
    tunjanganAnak=0
    status="Belum Menikah"

if(golongan=="A"):
    gajiPokok=10000000
    potongan=2.5
    jumlahTunjanganSuamiIstri=10000000*tunjanganSuamiIstri
    jumlahTunjanganAnak=10000000*tunjanganAnak
    gajiKotor=10000000+jumlahTunjanganSuamiIstri+jumlahTunjanganAnak
    jumlahPotongan=2.5/100*gajiKotor
    gajiBersih=gajiKotor-jumlahPotongan
elif(golongan=="B"):
    gajiPokok=8500000
    potongan=2.0
    jumlahTunjanganSuamiIstri=8500000*tunjanganSuamiIstri
    jumlahTunjanganAnak=8500000*tunjanganAnak
    gajiKotor=8500000+jumlahTunjanganSuamiIstri+jumlahTunjanganAnak
    jumlahPotongan=2.0/100*gajiKotor
    gajiBersih=gajiKotor-jumlahPotongan
elif(golongan=="C"):
    gajiPokok=7000000
    potongan=1.5
    jumlahTunjanganSuamiIstri=7000000*tunjanganSuamiIstri
    jumlahTunjanganAnak=7000000*tunjanganAnak
    gajiKotor=7000000+jumlahTunjanganSuamiIstri+jumlahTunjanganAnak
    jumlahPotongan=1.5/100*gajiKotor
    gajiBersih=gajiKotor-jumlahPotongan
elif(golongan=="D"):
    gajiPokok=5500000
    potongan=1.0
    jumlahTunjanganSuamiIstri=5500000*tunjanganSuamiIstri
    jumlahTunjanganAnak=5500000*tunjanganAnak
    gajiKotor=5500000+jumlahTunjanganSuamiIstri+jumlahTunjanganAnak
    jumlahPotongan=1.0/100*gajiKotor
    gajiBersih=gajiKotor-jumlahPotongan
    

print("======================================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("------------------------------------------------------")
print("Nama Karyawan         :",nama)
print("Golongan              :",golongan,"Kode:",kode)
print("Status                :",status)
print("Jumlah Anak           :",jumlahAnak)
print("------------------------------------------------------")
print("Gaji Pokok            :",gajiPokok)
print("Tunjangan Istri/Suami :",jumlahTunjanganSuamiIstri)
print("Tunjangan Anak        :",jumlahTunjanganAnak)
print("---------------------------------------------------- +")
print("Gaji Kotor            :",gajiKotor)
print("Potongan              :",jumlahPotongan)
print("---------------------------------------------------- -")
print("Gaji Bersih           :",gajiBersih)
