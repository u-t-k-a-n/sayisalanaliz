matris=[]
while True:
    try:
        mertebe=int(input("Lütfen matrisin satır sayısını giriniz:"))
        break
    except:
        print("Lütfen bir sayı giriniz.")
while mertebe<1:
    print("Satır sayısı pozitif olmalı.")
    while True:
        try:
            mertebe=int(input("Lütfen matrisin satır sayısını giriniz:"))
            break
        except:
            print("Lütfen bir sayı giriniz.")
for i in range(mertebe):
    satır=[]
    for j in range(mertebe):
        while True:
            try:
                eleman=float(input("Lütfen matrisin {}. satırın {}.elamanını giriniz:".format(i+1,j+1)))
                break
            except:
                print("Lütfen bir sayı giriniz.")
        satır.append(eleman)
    matris.append(satır)
birim=[]
for i in range(mertebe):
    satır=[]
    for j in range(mertebe):
        if i==j:
            satır.append(1)
        else:
            satır.append(0)
    birim.append(satır)
def satır_böl(satır,sayı):
    for i in range(len(satır)):
        satır[i]/=sayı
    return satır
def satır_satır(satır1,sayı,satır2):
    for i in range(len(satır1)):
         satır1[i]-=sayı*satır2[i]
    return satır1
for i in range(mertebe):
    sayı=matris[i][i]
    if sayı!=0:
        satır_böl(matris[i],sayı)
        satır_böl(birim[i],sayı)
    for j in range(mertebe):
        if i!=j:
            sayı=matris[j][i]
            satır_satır(matris[j],sayı,matris[i])
            satır_satır(birim[j],sayı,birim[i])
for i in range(mertebe):
    print(birim[i])

