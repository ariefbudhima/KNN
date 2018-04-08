import xlrd
from builtins import range, min

loc = "DatasetTugas3AI1718.xlsx"
workbook = xlrd.open_workbook(loc)
sheet = workbook.sheet_by_index(0)
sheety = workbook.sheet_by_index(1)

A1 = []
A2 = []
A3 = []
A4 = []
A5 = []
test1 = []
test2 = []
test3 = []
test4 = []
test5 = []
hasil = []
hasil1 = []
hasil2 = []
hasil3 = []
banding = []
tot = 0
fak = 0

kfold = sheet.nrows // 4
for i in range(1,1001):
    test1.append(sheety.cell_value(i,1))
    test2.append(sheety.cell_value(i,2))
    test3.append(sheety.cell_value(i,3))
    test4.append(sheety.cell_value(i,4))
    # test5.append(sheety.cell_value(i,5))

for i in range(1, 4 * kfold + 1):
    A1.append(sheet.cell_value(i, 1))
    A2.append(sheet.cell_value(i, 2))
    A3.append(sheet.cell_value(i, 3))
    A4.append(sheet.cell_value(i, 4))
    A5.append(sheet.cell_value(i, 5))
# print(len(A1))
data = [A1, A2, A3, A4, hasil]

# line 46-65 training
batas1 = 0
batas2 = 0
persentase = 0
for k in range(0,40):
    batas1 = batas2
    batas2 = batas2+100
    for j in range(batas1, batas2):
        for i in range(batas2, 4000):
            hasil = ((data[0][j] - data[0][i]) ** 2 + (data[1][j] - data[1][i]) ** 2 + (data[2][j] - data[2][i]) ** 2 + (data[3][j] - data[3][i]) ** 2) ** 0.5  # dapat 3k
            hasil1.append(hasil)
        # print(len(hasil1))
        if len(hasil1)<3900:
            for i in range(0,3900-len(hasil1)):
                hasil = ((data[0][j] - data[0][i]) ** 2 + (data[1][j] - data[1][i]) ** 2 + (
                data[2][j] - data[2][i]) ** 2 + (data[3][j] - data[3][i]) ** 2) ** 0.5  # dapat 3k
                hasil1.append(hasil)

        for i in range(0, 131):  # hitung k(pilih 101 terdekat)
            tot = tot + A5[hasil1.index(min(hasil1))]  # hitung kedekatan
            hasil1.remove(min(hasil1))
        if tot / 65 > 1:  # cek1 atau 0
            fak = 1
        banding.append(fak)  # masuk ke list banding
        tot = 0
        fak = 0
        hasil1.clear()

    persen = 0
    for i in range(0, 100):
        if banding[i] == A5[i+batas1]:
            persen = persen + 1
    print('persen = ', persen)
    persentase = persentase+persen
    i=0
    banding.clear()
print(persentase/40)

#line 83 testing
for j in range(0, 1000):
    for i in range(0, 4 * kfold):
        hasil = ((test1[j]-A1[i])**2+(test2[j]-A2[i])**2+(test3[j]-A3[i])**2+(test4[j]-A4[i])**2)**0.5
        hasil2.append(hasil)
    for i in range(0, 131):  # hitung k(pilih 101 terdekat)
        tot = tot + A5[hasil2.index(min(hasil2))]  # hitung kedekatan
        hasil2.remove(min(hasil2))
    if tot / 65 > 1:  # cek1 atau 0
        fak = 1
    test5.append(fak)  # masuk ke list test5
    tot = 0
    fak = 0
    hasil2.clear()

print(test5)