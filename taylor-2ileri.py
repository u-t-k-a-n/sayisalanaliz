fonksiyonlar={}
while True:
    try:
        max_derece=int(input("Lütfen fonksiyonunun en büyük derecesini giriniz:"))
        break
    except:
        print("Lütfen bir tam sayı giriniz.")
fonksiyonlar["fonksiyon"]=[]
for i in range(max_derece,-1,-1):
    while True:
        try:
            x = float(input("{}. dereceli terimin katsayısını giriniz:".format(i)))
            break
        except:
            print("Lütfen bir sayı giriniz.")
    fonksiyonlar["fonksiyon"].append(x)
yes_kök=input("Fonksiyon köklü ifade içeriyorsa evet yazın,içermiyorsa devam edin.")
yes_kök=yes_kök.upper()
if yes_kök=="EVET":
    while True:
        try:
            kök_derece=float(input("Lütfen kökün derecesini float biçiminde giriniz:"))
            break
        except:
            print("Lütfen bir sayı giriniz.")
    while True:
        try:
            kök_max=int(input("Lütfen kökün içerisindeki ifadenin en büyük derecesini giriniz:"))
            break
        except:
            print("Lütfen bir tam sayı giriniz.")
    while True:
        try:
            kök_min=int(input("Lütfen kökün içerisindeki ifadenin en küçük dereceyi giriniz:"))
            break
        except:
            print("Lütfen bir tam sayı giriniz.")
    fonksiyonlar["kök"]=[]
    for i in range(kök_max,kök_min-1,-1):
        while True:
            try:
                x=float(input("Kök içerisindeki ifadenin {}.dereceli olan terimin katsayısını giriniz:".format(i)))
                break
            except:
                print("Lütfen bir sayı giriniz.")
        fonksiyonlar["kök"].append(x)
yes_kesir=input("Fonksiyon kesirli ifade içeriyorsa evet yazın,içermiyorsa devam edin.")
yes_kesir=yes_kesir.upper()
if yes_kesir=="EVET":
    while True:
        try:
            pay_max=int(input("Lütfen paydaki ifadenin en büyük derecesini giriniz:"))
            break
        except:
            print("Lütfen bir tam sayı giriniz.")
    while True:
        try:
            pay_min=int(input("Lütfen paydaki ifadenin en küçük derecesini giriniz:"))
            break
        except:
            print("Lütfen bir tam sayı giriniz.")
    fonksiyonlar["pay"]=[]
    for i in range(pay_max,pay_min-1,-1):
        while True:
            try:
                x=float(input("Paydaki ifadenin {}. dereceli olan terimin katsayısını giriniz:".format(i)))
                break
            except:
                print("Lütfen bir sayı giriniz.")
        fonksiyonlar["pay"].append(x)
    while True:
        try:
            payda_max=int(input("Lütfen paydadaki ifadenin en büyük derecesini giriniz:"))
            break
        except:
            print("Lütfen bir tam sayı giriniz.")
    while True:
        try:
            payda_min=int(input("Lütfen paydadaki ifadenin en küçük derecesini giriniz:"))
            break
        except:
            print("Lütfen bir tam sayı giriniz.")
    fonksiyonlar["payda"]=[]
    for i in range(payda_max,payda_min-1,-1):
        while True:
            try:
                x=float(input("Paydadaki ifadenin {}. dereceli olan terimin katsayısını giriniz:".format(i)))
                break
            except:
                print("Lütfen bir sayı giriniz.")
        fonksiyonlar["payda"].append(x)
while True:
    try:
        start_x=float(input("Lütfen hangi noktanın türevinin alınacağını giriniz:"))
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
while True:
    try:
        delta=float(input("Lütfen delta değerini giriniz:"))
        break
    except:
        print("Lütfen bir sayı giriniz.")
if yes_kök=="EVET" and yes_kesir=="EVET":
    sum1=function(fonksiyonlar["fonksiyon"],start_x,max_derece)+\
             (function(fonksiyonlar["kök"],start_x,kök_max)**kök_derece)+ \
             (function(fonksiyonlar["pay"], start_x, pay_max) / function(fonksiyonlar["payda"],start_x, payda_max))
    sum2=function(fonksiyonlar["fonksiyon"],start_x+delta,max_derece)+\
             (function(fonksiyonlar["kök"],start_x+delta,kök_max)**kök_derece)+ \
             (function(fonksiyonlar["pay"], start_x+delta, pay_max) / function(fonksiyonlar["payda"],start_x+delta, payda_max))
    sum3 = function(fonksiyonlar["fonksiyon"], start_x +2* delta, max_derece) + \
           (function(fonksiyonlar["kök"], start_x +2* delta, kök_max) ** kök_derece) + \
           (function(fonksiyonlar["pay"], start_x + 2*delta, pay_max) / function(fonksiyonlar["payda"], start_x +2* delta,payda_max))
    sum=sum1-2*sum2+sum3
    sum/=delta**2
elif yes_kök=="EVET":
    sum1 = function(fonksiyonlar["fonksiyon"], start_x, max_derece) + \
           (function(fonksiyonlar["kök"], start_x, kök_max) ** kök_derece)
    sum2 = function(fonksiyonlar["fonksiyon"], start_x + delta, max_derece) + \
           (function(fonksiyonlar["kök"], start_x + delta, kök_max) ** kök_derece)
    sum3 = function(fonksiyonlar["fonksiyon"], start_x + 2 * delta, max_derece) + \
           (function(fonksiyonlar["kök"], start_x + 2 * delta, kök_max) ** kök_derece)
    sum = sum1 - 2 * sum2 + sum3
    sum /= delta ** 2
elif yes_kesir=="EVET":
    sum1 = function(fonksiyonlar["fonksiyon"], start_x, max_derece)+\
           (function(fonksiyonlar["pay"], start_x, pay_max) / function(fonksiyonlar["payda"], start_x, payda_max))
    sum2 = function(fonksiyonlar["fonksiyon"], start_x + delta, max_derece) + \
           (function(fonksiyonlar["pay"], start_x + delta, pay_max) / function(fonksiyonlar["payda"], start_x + delta,payda_max))
    sum3 = function(fonksiyonlar["fonksiyon"], start_x + 2 * delta, max_derece) + \
           (function(fonksiyonlar["pay"], start_x + 2 * delta, pay_max) / function(fonksiyonlar["payda"],start_x + 2 * delta, payda_max))
    sum = sum1 - 2 * sum2 + sum3
    sum /= delta ** 2
print("{} noktasındaki 2. türevin değeri:{}".format(start_x,sum))