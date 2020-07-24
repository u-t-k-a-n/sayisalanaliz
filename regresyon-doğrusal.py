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
matris=[[n,sum(x_ler)],[sum(x_ler),sum(i*i for i in x_ler)]]
sonuç=[sum(y_ler),sum(x_ler[i]*y_ler[i] for i in range(n))]
for i in range(2):
    bölen=matris[i][i]
    for j in range(2):
        matris[i][j]/=bölen
    sonuç[i]/=bölen
    for j in range(i+1,2):
        bölen=matris[j][i]
        for k in range(2):
            matris[j][k]/=bölen
            matris[i+1][k]-=matris[i][k]
        sonuç[j]/=bölen
        sonuç[i+1]-=sonuç[i]
        for k in range(2):
            matris[j][k]*=bölen
        sonuç[j]*=bölen
for i in range(1,0,-1):
    for j in range(i-1,-1,-1):
        sonuç[j]-=sonuç[i+1]*matris[j][i]
if sonuç[1]>0:
    print("y= {} + {}x".format(sonuç[0],sonuç[1]))
elif sonuç[1]<0:
    print("y= {}{}x".format(sonuç[0], sonuç[1]))
predict=lambda x:sonuç[0]+sonuç[1]*x
while True:
    try:
        x=float(input("Hesaplanmasını istediğiniz değeri giriniz:"))
        break
    except:
        print("Lütfen bir sayı giriniz.")
print("{} noktasındaki değer:{}".format(x,predict(x)))