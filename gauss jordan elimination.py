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
for i in range(mertebe-1,0,-1):
    for j in range(i-1,-1,-1):
        denklem[j]-=denklem[i+1]*matris[j][i]
for i in range(mertebe):
    print("{}. bilinmeyenin değeri: {}".format(i+1,denklem[i]))