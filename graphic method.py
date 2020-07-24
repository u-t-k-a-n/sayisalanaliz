import time
fonksiyon=[]
while True:
    try:
        max_derece=int(input("Lütfen fonksiyonun en büyük derecesini giriniz:"))
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
        first_x=float(input("Lütfen başlangıç değerini giriniz:"))
        break
    except:
        print("Lütfen bir sayı giriniz.")
while True:
    try:
        delta_x = float(input("Lütfen x'in artış miktarını giriniz:"))
        break
    except:
        print("Lütfen bir sayı giriniz.")
while True:
    try:
        epsilon = float(input("Lütfen epsilon değerini giriniz:"))
        break
    except:
        print("Lütfen bir sayı giriniz.")
def function(fonksiyon,first_x,max_derece):
    sum=0
    j=0
    for i in fonksiyon:
        sum+=(i*(first_x**(max_derece-j)))
        j+=1
    return sum
sum1 = function(fonksiyon, first_x, max_derece)
sum2 = function(fonksiyon, first_x + delta_x, max_derece)
if sum1==0:
    print("Kök:",first_x)
if sum2==0:
    print("Kök:",first_x+delta_x)
if sum1!=0 and sum2!=0:
    while abs(delta_x)>epsilon and sum2!=0:
        sum1 = function(fonksiyon, first_x, max_derece)
        sum2 = function(fonksiyon, first_x + delta_x, max_derece)
        if time.process_time()==5:
            print("KÖK YOK!!!!!!!!!!!!!!")
            raise Exception("Kök yok.")
        while (sum1*sum2)>0:
            if time.process_time() == 5:
                print("KÖK YOK!!!!!!!!!!!!!!")
                raise Exception("Kök yok.")
            sum1=sum2
            first_x+=delta_x
            sum2 = function(fonksiyon, first_x+delta_x, max_derece)
        delta_x/=2
    if sum2==0:
        print("Kök:",first_x+2*delta_x)
    else:
        if delta_x>0:
            print("Kök [{},{}] aralığındadır.".format(first_x,first_x+delta_x))
        elif delta_x<0:
            print("Kök [{},{}] aralığındadır.".format(first_x+delta_x, first_x))
