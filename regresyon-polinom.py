while True:
    try:
        n=int(input("Lütfen gözlem sayısını giriniz:"))
        break
    except:
        print("Lütfen bir sayı giriniz.")
while n<1:
    print("Gözlem sayısı 1'den küçük olamaz.")
    while True:
        try:
            n = int(input("Lütfen gözlem sayısını giriniz:"))
            break
        except:
            print("Lütfen bir sayı giriniz.")
x_ler=[]
y_ler=[]
for i in range(n):
    while True:
        try:
            x =float(input("Lütfen {}. x değerini giriniz:".format(i+1)))
            break
        except:
            print("Lütfen bir sayı giriniz.")
    x_ler.append(x)
for i in range(n):
    while True:
        try:
            y =float(input("Lütfen {}. y değerini giriniz:".format(i+1)))
            break
        except:
            print("Lütfen bir sayı giriniz.")
    y_ler.append(y)
while True:
    try:
        derece=int(input("Lütfen polinomun en büyük derecesini giriniz:"))
        break
    except:
        print("Lütfen bir sayı giriniz.")
derece+=1
matris=[]
for i in range(derece):
    satır=[]
    for j in range(derece):
        satır.append(sum(k**(i+j) for k in x_ler))
    matris.append(satır)
sonuç=[]
for i in range(derece):
    sonuç.append(sum(j*(k**i) for (j,k) in (y_ler,x_ler)))
for i in range(derece):
    bölen=matris[i][i]
    for j in range(derece):
        matris[i][j]/=bölen
    sonuç[i]/=bölen
    for j in range(i+1,derece):
        bölen=matris[j][i]
        for k in range(derece):
            matris[j][k]/=bölen
            matris[i+1][k]-=matris[i][k]
        sonuç[j]/=bölen
        sonuç[i+1]-=sonuç[i]
        for k in range(derece):
            matris[j][k]*=bölen
        sonuç[j]*=bölen
for i in range(1,0,-1):
    for j in range(i-1,-1,-1):
        sonuç[j]-=sonuç[i+1]*matris[j][i]
for i in range(derece):
    print("{}. dereceli katsayı:{}".format(i,sonuç[i]))
predict=lambda x:sum(sonuç[i]*(x**i) for i in range(derece))
while True:
    try:
        x=float(input("Hesaplanmasını istediğiniz değeri giriniz:"))
        break
    except:
        print("Lütfen bir sayı giriniz.")
print("{} noktasındaki değer:{}".format(x,predict(x)))