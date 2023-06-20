def addMahasiswa():
    jumlah = int(input("Jumlah mahasiswa: "))
    mahasiswa = []
    while jumlah > 0:
        nama = input("Nama mahasiswa: ")
        mahasiswa.append(nama)
        jumlah -= 1
    
    panggil(mahasiswa)

def removeMahasiswa(arrayMahasiswa):
    print("Data mahasiswa %s" % arrayMahasiswa)
    mahasiswa = input("Hapus mahasiswa: ")
    arrayMahasiswa.remove(mahasiswa)
    print("Data Mahasiswa %s" % arrayMahasiswa)
    panggil(arrayMahasiswa)

def ascMahasiswa(arrayMahasiswa):
    arrayMahasiswa.sort()
    print(arrayMahasiswa)
    panggil(arrayMahasiswa)

def viewMahasiswa(arrayMahasiswa):
    for x in arrayMahasiswa:
        print("Nama Mahasiswa %s" % x)
    panggil(arrayMahasiswa)

def panggil(arrayMahasiswa):
    print("\n<=========Menu Data Mahasiswa=========>")
    print("1. Tambah Data Mahasiswa")
    print("2. Hapus Data Mahasiswa")
    print("3. Urutkan Data Mahasiswa")
    print("4. Lihat Data Mahasiswa")
    print("5. Tutup")

    pilih = int(input("Pilih: "))
    if pilih == 1:
        addMahasiswa()
    elif pilih == 2:
        removeMahasiswa(arrayMahasiswa)
    elif pilih == 3:
        ascMahasiswa(arrayMahasiswa)
    elif pilih == 4:
        viewMahasiswa(arrayMahasiswa)
    else:
        print("Selesai")

panggil([])

def insertion_sort(array):
    for i in range(1, len(array)):
        item = array[i]
        j = i - 1

        while j >= 0 and array[j] > item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = item

    return array

# 


#####




# def bubble_sort(array):
#     for i in range(len(array)):
#         for j in range(len(array)-i-1):
#             if array[j]<array[j+1]:
#                 array[j],array[j+1]=array[j+1],array[j]

#     return array
# array2=[12,19,20,22,11,28,33]
# bubble_sort(array2)
# print(array2)

# def selection_sort(array):
#     for i in range(len(array)):
#         min_index = i
#         for j in range(i + 1, len(array)):
#             if array[min_index] < array[j]:
#                 min_index = j
#         array[i], array[min_index] = array[min_index], array[i]

# array2 = [12, 19, 20, 22, 11, 28, 33]
# selection_sort(array2)
# print(array2)

