#Praktikum 2
#Nomor dua
i=0
while(i<10):
    print('Hello World')
    i+=1
    
print()

#Nomor lima
i=2
while(i<=20):
    print('Hello World')
    i+=2

print()

#Nomor enam
i=0
while True:
    print('Hello World')
    i+=1
    if(i==10):
        break

print()

#Nomor delapan
#kotak bintang ajaib
kolom=5
baris=5

i=0
while(i<baris):
    j=0
    while(j<kolom):
        print('*',end='')
        j+=1
    print('')
    i+=1

print()

#Nomor sepuluh
kolom=i
baris=j
for i in range(5):
    for j in range(i+1):
        print('*',end='')
    print()
    
print()

#Nomor sebelas
from random import randint
while True:
    bil=randint(0,10)
    print(bil)
    if bil==5:
        break
    
print()

#Nomor tigabelas
sum=0
from random import randint
while True:
    bil=randint(0,10)
    print(bil)
    if bil==5:
        break
    sum=sum+1
print("Jumlah perulangan:",str(sum))

print()

#Latihan
#Nomor satu
for i in range(1,100,2):
        print(i)

print()

#Nomor dua
sum=0
for i in range(1,100,2):
        print(i)
        sum=sum+1
print("Banyaknya bilangan ganjil:",str(sum))

print()

#Nomor tiga
sum=0
hitung=0
for i in range(1,100,2):
        print(i)
        sum=sum+1
        bil=i+1
        hitung=hitung+bil
print("Banyaknya bilangan ganjil:",str(sum))
print("Jumlah seluruh bilangan:",str(hitung))

print()

#Nomor empat
kolom=i
baris=j
for i in reversed(range(5)):
    for j in range(i+1):
        print('*',end='')
    print()

print()

#Nomor lima
print("Hai...nama saya Mr. Lapple, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silahkan tebak ya!")
from random import randint
angka=randint(0,100)
bil=-1
while bil!=angka:
    bil=int(input("Masukkan bilangan:"))
    if(bil==angka):
        print("Yee...Bilangan tebakan anda BENAR")
    elif(bil>angka):
        print("Hehehe...Bilangan tebakan anda terlalu besar")
    else:
        print("Hehehe...Bilangan tebakan anda terlalu kecil")

print()

#Nomor enam
print("Hai...nama saya Mr. Lapple, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silahkan tebak ya!")
from random import randint
angka=randint(0,100)
bil=-1
while bil!=angka:
    bil=int(input("Masukkan bilangan:"))
    if(bil==angka):
        print("Yee...Bilangan tebakan anda BENAR")
    elif(bil>angka):
        print("Hehehe...Bilangan tebakan anda terlalu besar")
    else:
        print("Hehehe...Bilangan tebakan anda terlalu kecil")

scoreAwal=100
salah=-2
totalScore=scoreAwal+salah
print("Score anda:",totalScore)
