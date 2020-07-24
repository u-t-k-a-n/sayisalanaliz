fonksiyon=[]
while True:
    try:
        max_derece = int(input("Lütfen fonksiyonun en büyük derecesini giriniz:"))
        break
    except:
        print("Lütfen bir tam sayı giriniz.")
while True:
    try:
        min_derece=int(input("Lütfen fonksiyonun en düşük derecesini giriniz:"))
        break
    except:
        print("Lütfen bir tam sayı giriniz.")
for i in range(max_derece,min_derece-1,-1):
    while True:
        try:
            x = float(input("{}. dereceli terimin katsayını giriniz:".format(i)))
            break
        except:
            print("Lütfen bir sayı giriniz.")
    fonksiyon.append(x)
while True:
    try:
        start_x=float(input("Lütfen başlangıç değerini giriniz:"))
        break
    except:
        print("Lütfen bir sayı giriniz.")
while True:
    try:
        end_x=float(input("Lütfen bitiş değerini giriniz:"))
        break
    except:
        print("Lütfen bir sayı giriniz.")
while True:
    try:
        delta=float(input("Lütfen delta değerini giriniz."))
        break
    except:
        print("Lütfen bir sayı giriniz.")
def function(fonksiyon,x,max_derece):
    sum=0
    j=0
    for i in fonksiyon:
        sum+=(i*(x**(max_derece-j)))
        j+=1
    return sum
i=start_x
tablo={}
tablo["x_ler"]=[]
tablo["fark0"]=[]
while i<end_x:
    tablo["x_ler"].append(i)
    tablo["fark0"].append(function(fonksiyon,i,max_derece))
    i+=delta
def control(list):
    sum=0
    for i in range(len(list)-1):
        if list[i]==list[i+1]:
            sum+=1
    return sum
liste=tablo["fark0"].copy()
i=1
while control(liste)!=len(liste)-1:
   tablo["fark{}".format(i)]=[]
   for j in range(len(liste)-1):
       tablo["fark{}".format(i)].append(liste[j+1]-liste[j])
   liste=tablo["fark{}".format(i)].copy()
   i+=1
print("----------------------İLERİ FARK TABLOSU----------------------")
print("x değerleri:",tablo["x_ler"])
print("Fonksiyon sonuçları:",tablo["fark0"])
for j in range(1,i-1):
    print("{}. ileri fark:{}".format(j,tablo["fark{}".format(j)]))