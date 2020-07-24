matris=[]
while True:
    try:
        mertebe=int(input("Lütfen katsayılar matrisinin satır sayısını giriniz:"))
        break
    except:
        print("Lütfen bir sayı giriniz.")
while mertebe<1:
    print("Satır sayısı pozitif olmalı.")
    while True:
        try:
            mertebe=int(input("Lütfen katsayılar matrisinin satır sayısını giriniz:"))
            break
        except:
            print("Lütfen bir sayı giriniz.")
for i in range(mertebe):
    satır=[]
    for j in range(mertebe):
        while True:
            try:
                eleman=float(input("Lütfen katsayılar matrisinin {}. satırının {}.elamanını giriniz:".format(i+1,j+1)))
                break
            except:
                print("Lütfen bir sayı giriniz.")
        satır.append(eleman)
    matris.append(satır)
denklem=[]
for i in range(mertebe):
    while True:
        try:
            değer=float(input("Lütfen {}. denklemin sağ tarafındaki değeri giriniz:".format(i+1)))
            break
        except:
            print("Lütfen bir sayı giriniz.")
    denklem.append(değer)
for i in range(mertebe):
    bölen=matris[i][i]
    for j in range(mertebe):
        matris[i][j]/=bölen
    denklem[i]/=bölen
    for j in range(i+1,mertebe):
        bölen=matris[j][i]
        for k in range(mertebe):
            matris[j][k]/=bölen
            matris[i+1][k]-=matris[i][k]
        denklem[j]/=bölen
        denklem[i+1]-=denklem[i]
        for k in range(mertebe):
            matris[j][k]*=bölen
        denklem[j]*=bölen
x_ler=[0]
x_ler*=mertebe
x_ler[-1]=denklem[-1]
for i in range(mertebe-2,-1,-1):
    sum=0
    for j  in range(i+1,mertebe):
        sum+=matris[i][j]*x_ler[i]
    x_ler[i]=denklem[i]-sum
for i in range(mertebe):
    print("{}. bilinmeyenin değeri: {}".format(i+1,x_ler[i]))