from itertools import permutations
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
sonuç=[]
for i in range(mertebe):
    while True:
        try:
            değer=float(input("Lütfen {}. denklemin sağ tarafındaki değeri giriniz:".format(i+1)))
            break
        except:
            print("Lütfen bir sayı giriniz.")
    sonuç.append(değer)
while True:
    try:
        epsilon=float(input("Lütfen epsilon değerini giriniz:"))
        break
    except:
        print("Lütfen bir sayı giriniz.")
while epsilon<=0:
    print("Epsilon değeri 0'dan küçük olamaz.")
    try:
        epsilon = float(input("Lütfen epsilon değerini giriniz:"))
        break
    except:
        print("Lütfen bir sayı giriniz.")
başlangıç=[]
for i in range(mertebe):
    while True:
        try:
            x=float(input("Lütfen {}. değişkenin başlangıç değerini giriniz:".format(i+1)))
            break
        except:
            print("Lütfen bir sayı giriniz.")
    başlangıç.append(x)
max=0
sum=1
per_mat=list(permutations(matris))
per_son=list(permutations(sonuç))
for i in range(len(per_mat)):
    for j in range(mertebe):
        sum*=abs(per_mat[i][j][j])
    if max<sum:
        max=sum
        index=i
    sum=1
if max==0:
    raise Exception("Bu matris bu yolla çözülemez.")
def function(başlangıç):
    it=[]
    for i in range(mertebe):
        sum=per_son[index][i]
        for j in range(mertebe):
            if i!=j:
                sum-=başlangıç[j]*per_mat[index][i][j]
        sum/=per_mat[index][i][i]
        it.append(sum)
    return it
it1=function(başlangıç)
def function2(iter):
    it = iter.copy()
    for i in range(mertebe):
        sum = per_son[index][i]
        for j in range(mertebe):
            if i != j:
                sum -= it[j] * per_mat[index][i][j]
        sum /= per_mat[index][i][i]
        it[i]=sum
    return it
it2=function2(it1)
delta=[abs(it1[i]-it2[i]) for i in range(mertebe)]
def control():
    sum=0
    for i in delta:
        if i>epsilon:
            sum+=1
    return sum
while control()>0:
    it1 = function2(it2)
    it2 = function2(it1)
    delta = [abs(it1[i] - it2[i]) for i in range(mertebe)]
for i in range(mertebe):
    print("{}. değişkenin değeri:{}".format(i+1,it2[i]))
