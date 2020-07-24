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
while end_x<start_x:
    print("Başlangıç değeri bitiş değerinden büyük olamaz.")
    while True:
        try:
            start_x = float(input("Lütfen başlangıç değerini giriniz:"))
            break
        except:
            print("Lütfen bir sayı giriniz.")
    while True:
        try:
            end_x = float(input("Lütfen bitiş değerini giriniz:"))
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
sum_start=function(fonksiyon,start_x,max_derece)
sum_end=function(fonksiyon,end_x,max_derece)
if sum_start==0:
    print("Kök:",start_x)
if sum_end==0:
    print("Kök:",end_x)
if sum_start*sum_end>0:
    print("[{},{}] aralığında kök yok.".format(start_x,end_x))
elif sum_start*sum_end<0:
    lineer_x1=((end_x*abs(sum_start))+(start_x*abs(sum_end)))/(abs(sum_start)+abs(sum_end))
    sum_lineer=function(fonksiyon,lineer_x1,max_derece)
    if sum_lineer==0:
        print("Kök:",lineer_x1)
    else:
        if sum_start*sum_lineer<0:
            end_x=lineer_x1
        elif sum_end*sum_lineer<0:
            start_x=lineer_x1
        lineer_x2 =((end_x*abs(sum_start))+(start_x*abs(sum_end)))/(abs(sum_start)+abs(sum_end))
        sum_lineer = function(fonksiyon, lineer_x2, max_derece)
        while (abs(lineer_x1-lineer_x2)>epsilon and sum_lineer!=0):
            lineer_x2 = ((end_x*abs(sum_start))+(start_x*abs(sum_end)))/(abs(sum_start)+abs(sum_end))
            sum_lineer = function(fonksiyon, lineer_x2, max_derece)
            if sum_start*sum_lineer<0:
                end_x=lineer_x2
            elif sum_end*sum_lineer<0:
                start_x=lineer_x2
            sum_start=function(fonksiyon,start_x,max_derece)
            sum_end=function(fonksiyon,end_x,max_derece)
            lineer_x1 = ((end_x*abs(sum_start))+(start_x*abs(sum_end)))/(abs(sum_start)+abs(sum_end))
            sum_lineer = function(fonksiyon, lineer_x1, max_derece)
        if sum_lineer==0:
            print("Kök:",lineer_x1)
        elif abs(lineer_x1-lineer_x2)<=epsilon:
            print("Kökün yaklaşık değeri:",round(lineer_x1,2))
