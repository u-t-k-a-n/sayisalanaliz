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
        start_x=float(input("Lütfen alt aralık değerini giriniz:"))
        break
    except:
        print("Lütfen bir sayı giriniz.")
while True:
    try:
        end_x=float(input("Lütfen üst aralık değerini giriniz:"))
        break
    except:
        print("Lütfen bir sayı giriniz.")
while True:
    try:
        n=int(input("Lütfen adım sayısını çift sayı olacak şekilde giriniz:"))
        break
    except:
        print("Lütfen bir sayı giriniz.")
while n%2!=0:
    try:
        n = int(input("Lütfen adım sayısını çift sayı olacak şekilde giriniz:"))
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
delta=(end_x-start_x)/n
sum=function(fonksiyon,start_x,max_derece)+function(fonksiyon,end_x,max_derece)
sum1=0
for i in range(1,n,2):
    sum1+=function(fonksiyon,start_x+i*delta,max_derece)
sum2=0
for i in range(2,n-1,2):
    sum2+=function(fonksiyon,start_x+i*delta,max_derece)
sum+=(delta/3)*(4*sum1+2*sum2)
print("İntegralin değeri:",sum)