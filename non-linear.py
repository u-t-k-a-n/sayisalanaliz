while True:
    try:
        mertebe=int(input("Lütfen değişken sayısını giriniz:"))
        break
    except:
        print("Lütfen bir sayı giriniz.")
while mertebe<1:
    print("Değişken sayısı 1'den küçük olamaz.")
    try:
        mertebe=int(input("Lütfen değişken sayısını giriniz:"))
        break
    except:
        print("Lütfen bir sayı giriniz.")
matris_ksayı=[]
matris_derece=[]
sabitler=[]
for i in range(mertebe):
    satır_ksayı=[]
    satır_derece=[]
    for j in range(mertebe):
        while True:
            try:
                ksayı=float(input("Lütfen matrisin {}. satırının {}. değişkeninin katsayısını giriniz:".format(i+1,j+1)))
                break
            except:
                print("Lütfen bir sayı giriniz.")
        satır_ksayı.append(ksayı)
        while True:
            try:
                derece=float(input("Lütfen matrisin {}. satırının {}. değişkeninin derecesini giriniz:".format(i+1,j+1)))
                break
            except:
                print("Lütfen bir sayı giriniz.")
        satır_derece.append(derece)
    matris_ksayı.append(satır_ksayı)
    matris_derece.append(satır_derece)
    while True:
        try:
            sabit=float(input("Lütfen {}. fonksiyonun sabit sayısının değerini giriniz:".format(i+1)))
            break
        except:
            print("Lütfen bir sayı giriniz")
başlangıç=[]
for i in range(mertebe):
    while True:
        try:
            x=float(input("Lütfen {}. değişkenin başlangıç değerini giriniz:".format(i+1)))
            break
        except:
            print("Lütfen bir sayı giriniz.")
    başlangıç.append(x)
while True:
    try:
        epsilon=float(input("Lütfen epsilon değerini giriniz:"))
        break
    except:
        print("Lürfen bir sayı giriniz.")
türev=lambda katsayı,x,derece:katsayı*derece*(x**(derece-1))
fonksiyon=lambda katsayı,x,derece:katsayı*(x**derece)
matris_türev=[]
for i in range(mertebe):
    satır=[]
    for j in range(mertebe):
        satır.append(türev(matris_ksayı[i][j],başlangıç[j],matris_derece[i][j]))
    matris_türev.append(satır)
list_fonksiyon=[]
for i in range(mertebe):
    for j in range(mertebe):
        sum=0
        sum+=fonksiyon(matris_ksayı[i][j],başlangıç[j],matris_derece[i][j])
        sum+=sabitler[i]
    list_fonksiyon.append(-sum)
for i in range(mertebe):
    bölen=matris_türev[i][i]
    for j in range(mertebe):
        matris_türev[i][j]/=bölen
    list_fonksiyon[i]/=bölen
    for j in range(i+1,mertebe):
        bölen=matris_türev[j][i]
        for k in range(mertebe):
            matris_türev[j][k]/=bölen
            matris_türev[i+1][k]-=matris_türev[i][k]
        list_fonksiyon[j]/=bölen
        list_fonksiyon[i+1]-=list_fonksiyon[i]
        for k in range(mertebe):
            matris_türev[j][k]*=bölen
        list_fonksiyon[j]*=bölen
delta=[0]
delta*=mertebe
delta[-1]=list_fonksiyon[-1]
for i in range(mertebe-2,-1,-1):
    sum=0
    for j  in range(i+1,mertebe):
        sum+=matris_türev[i][j]*delta[i]
    delta[i]=list_fonksiyon[i]-sum
def control():
    sum=0
    for i in delta:
        if i>epsilon:
            sum+=1
    return sum
while control()>0:
    for i in range(mertebe):
        satır = []
        for j in range(mertebe):
            satır.append(türev(matris_ksayı[i][j], başlangıç[j]+delta[j], matris_derece[i][j]))
        matris_türev[i]=satır
    for i in range(mertebe):
        for j in range(mertebe):
            sum = 0
            sum += fonksiyon(matris_ksayı[i][j], başlangıç[j]+delta[j], matris_derece[i][j])
            sum += sabitler[i]
        list_fonksiyon[i]=-sum
    for i in range(mertebe):
        bölen=matris_türev[i][i]
        for j in range(mertebe):
            matris_türev[i][j]/=bölen
        list_fonksiyon[i]/=bölen
        for j in range(i+1,mertebe):
            bölen=matris_türev[j][i]
            for k in range(mertebe):
                matris_türev[j][k]/=bölen
                matris_türev[i+1][k]-=matris_türev[i][k]
            list_fonksiyon[j]/=bölen
            list_fonksiyon[i+1]-=list_fonksiyon[i]
            for k in range(mertebe):
                matris_türev[j][k]*=bölen
            list_fonksiyon[j]*=bölen
    delta[-1]=list_fonksiyon[-1]
    for i in range(mertebe-2,-1,-1):
        sum=0
        for j  in range(i+1,mertebe):
            sum+=matris_türev[i][j]*delta[i]
        delta[i]=list_fonksiyon[i]-sum
    for i in range(mertebe):
        başlangıç[i]+=delta[i]
for i in range(mertebe):
    print("{}. değişkenin değeri:{}".format(i+1,başlangıç[i]))
