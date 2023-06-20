#validasi nilai pada proses pembagian bilangan
while True:
    bil = int(input("Masukkan bilangan yang akan dibagi : "))
    pembagi = int(input("Masukkan bilangan pembagi : "))

    if(pembagi == 0):
        print("Pembagi tidak boleh 0")
    else:
        hasil = bil*pembagi
        print("Hasil bagi : ",hasil)
        