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
def üst_üçgen_matris(matrix,mertebe):
    for i in range(mertebe-1):
        for j in range(i+1,mertebe):
            if matrix[i][i]==0:
                matrix[i][i]=10**-18
            sayı=matrix[j][i]/matrix[i][i]
            for k in range(mertebe):
                matrix[j][k]-=sayı*matrix[i][k]
    return matrix
def determinant(matrix,mertebe):
    if mertebe==1:
        return matrix[0]
    else:
        üst_üçgen_matris(matrix,mertebe)
        det=1
        for i in range(mertebe):
            det*=matrix[i][i]
    return det
işlem_matris=list(map(list,matris))
detA=determinant(işlem_matris,mertebe)
if detA==0:
    print("Çözüm yok.")
else:
    for i in range(mertebe):
        değer_matris=list(map(list,matris))
        for j in range(mertebe):
            değer_matris[j][i]=denklem[j]
        print("{}. bilinmeyenin değeri:".format(i+1),determinant(değer_matris,mertebe)/detA)


