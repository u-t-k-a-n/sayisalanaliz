while True:
    try:
        n=int(input("Lütfen n sayısının değerini giriniz:"))
        break
    except:
        print("Lütfen bir sayı giriniz.")
x_ler=[]
for i in range(n+1):
    while True:
        try:
            x=float(input("Lütfen {}. x değerini giriniz:".format(i)))
            break
        except:
            print("Lütfen bir sayı giriniz.")
    x_ler.append(x)
y_ler=[]
for i in range(n+1):
    while True:
        try:
            y=float(input("Lütfen {}. y değerini giriniz:".format(i)))
            break
        except:
            print("Lütfen bir sayı giriniz.")
    y_ler.append(y)
while True:
    try:
        x=float(input("Lütfen fonksiyonun hesaplanmasını istediğiniz noktayı giriniz:"))
        break
    except:
        print("Lütfen bir sayı giriniz.")
def lagrange_ksayı(x,i):
    sum=1
    for j in range(n+1):
        if i!=j:
            sum*=(x-x_ler[j])/(x_ler[i]-x_ler[j])
    return sum
sum=0
for i in range(n+1):
    tmp=lagrange_ksayı(x,i)*y_ler[i]
    sum+=tmp
print("Fonksiyonun {} noktasındaki değeri:{}".format(x,sum))