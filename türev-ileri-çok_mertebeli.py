from math import factorial
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
while True:
    try:
        türev_mertebe=int(input("Lütfen kaçıncı dereceden türevin hesaplnacağını giriniz:"))
        break
    except:
        print("Lütfen bir sayı giriniz.")
sonuç=[]
if yes_kök=="EVET" and yes_kesir=="EVET":
    for i in range(türev_mertebe+1):
        com=factorial(türev_mertebe)/(factorial(i)*factorial(türev_mertebe-i))
        com*=(-1)**i
        sum=function(fonksiyonlar["fonksiyon"],türev_mertebe*start_x-i,max_derece)+\
             (function(fonksiyonlar["kök"],türev_mertebe*start_x-i,kök_max)**kök_derece)+ \
             (function(fonksiyonlar["pay"],türev_mertebe*start_x-i, pay_max) / function(fonksiyonlar["payda"],türev_mertebe*start_x-i, payda_max))
        sum*=com
        sonuç.append(sum)
elif yes_kök=="EVET":
    for i in range(türev_mertebe + 1):
        com = factorial(türev_mertebe) / (factorial(i) * factorial(türev_mertebe - i))
        com *= (-1) ** i
        sum = function(fonksiyonlar["fonksiyon"], türev_mertebe * start_x - i, max_derece) + \
              (function(fonksiyonlar["kök"], türev_mertebe * start_x - i, kök_max) ** kök_derece)
        sum *= com
        sonuç.append(sum)
elif yes_kesir=="EVET":
    for i in range(türev_mertebe + 1):
        com = factorial(türev_mertebe) / (factorial(i) * factorial(türev_mertebe - i))
        com *= (-1) ** i
        sum = function(fonksiyonlar["fonksiyon"], türev_mertebe * start_x - i, max_derece) + \
              (function(fonksiyonlar["pay"],türev_mertebe*start_x-i,pay_max) / function(fonksiyonlar["payda"],türev_mertebe*start_x-i,payda_max))
        sum *= com
        sonuç.append(sum)
print("{} noktasındaki {}. türevin değeri:{}".format(start_x,türev_mertebe,sum(sonuç)))