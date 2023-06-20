#GUIDED
#percabangan if satu kondisi
nilai = int(input("Masukkan bilangan bulat : "))

if (nilai > 0) :
    print("Bilangan ", nilai," merupakan bilangan bulat")

#percabangan if dua kondisi
bilangan = int(input("Masukkan Bilangan : "))

if(bilangan % 2 == 0):
    print("Bilangan ",bilangan," merupakan bilangan genap")
else:
    print("Bilangan",bilangan," merupakan bilangan ganjil")

#percabangan if tiga kondisi atau lebih
bilangan = int(input("Masukkan Bilangan : "))

if(bilangan>0):
    print(bilangan," merupakan bilangan positif")
elif(bilangan<0):
    print(bilangan," merupakan bilangan negatif")
else:
    print(bilangan," merupakan blangan nol")

#menentukan wujud air sesuai suhu
input = int(input("Masukkan suhu air : "))

if(suhu<=0):
    print("Pada suhu ",suhu," derajat celcius, air akan berwujud es")
elif(suhu>0 & suhu<100):
    print("Pada suhu ",suhu," derajat celcius, air akan berwujud air")
else:
    print("Pada suhu ",suhu," derajat celcius, air akan berwujud gas")


#menentukan panggilan seseorang
gender = int(input("Perempuan atau Laki-laki (L/P)"))

if(gender == "L"):
    status = input("Anda sudah menikah atau belum? (Y/N)")
    if(status == "Y"):
        print("Hallo Bapak!")
    elif(status == "N"):
        print("Hallo Mas!")
    else:
        print("Tidak ada dalam pilihan")
elif(gender == "P"):
    status = input("Anda sudah menikah atau belum? (Y/N)")
    if(status == "Y"):
        print("Hallo Ibu!")
    elif(status == "N"):
        print("Hallo Mba!")
    else:
        print("Tidak ada dalam pilihan")
else:
    print("Tidak ada dalam pilihan")


#program inputan data diri
print("=====INPUT=====")
nama = input("Nama  : ")
jk = input("Jenis Kelamin (L/P) : ")
print("1.Islam\n2Protestan\n3.katolik\n4.Hindu\n5.Budha")
agama = int(input("Agama : "))
#1=Islam, 2=Protestan, 3=katolik, 4=Hindu, 5=Budha
if(agama==1):
    agama = "Islam"
elif(agama==2):
    agama = "Protestan"
elif(agama==3):
    agama = "Katolik"
elif(agama==4):
    agama = "Hindu"
elif(agama==5):
    agama = "Budha"
else:
    print("Agama tidak ditemukan")

print("=====OUTPUT=====")
print("Nama : ",nama)
print("Jenis Kelamin : ",jk)
print("Agama : ",agama)


   
