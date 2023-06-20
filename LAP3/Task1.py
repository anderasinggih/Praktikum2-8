#menentukan huruf vokal dan konsonan

huruf = input("Masukkan sebuah huruf : ")

vokal = ['a','i','u','e','o']
if(huruf.lower()in vokal):
    print(huruf," Adalah salah satu huruf vokal")
else:
    print(huruf," Adalah salah satu huruf konsonan")
