import time
result = time.localtime()
saat = int(input("lutfen saati Türk saati olarak giriniz:"))

if(8 <= saat < 12):
    print("Günaydın")
elif(12 <= saat < 16):
    print("Hayırlı Günler")
elif(16 <= saat < 22):
    print("Hayırlı Akşamlar")
elif(22 <= saat < 1):
    print("Hayırlı Geceler")
else:
    print("Hatalı saat girdiniz :( ")
