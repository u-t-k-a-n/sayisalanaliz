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
        epsilon = float(input("Lütfen epsilon değerini giriniz:"))
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
def türev(fonksiyon,x,max_derece):
    sum=0
    j=0
    for i in fonksiyon:
        sum+=(i*(max_derece-j)*(x**(max_derece-j-1)))
        j+=1
    return sum
sum1=function(fonksiyon,start_x,max_derece)
if sum1==0:
    print("Kökün değeri:",start_x)
else:
    second_x=start_x-(function(fonksiyon,start_x,max_derece)/türev(fonksiyon,start_x,max_derece))
    while abs(second_x-start_x)>epsilon and sum1!=0:
        start_x=second_x
        second_x = start_x - (function(fonksiyon, start_x, max_derece) / türev(fonksiyon, start_x, max_derece))
        sum1=function(fonksiyon,second_x,max_derece)
    if sum1==0:
        print("Kökün değeri:",second_x)
    else:
        print("Kökün yaklaşık değeri:",round(second_x,2))