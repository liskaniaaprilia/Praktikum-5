no = 0
lanjut = 'ya'
nama = []
nim = []
uts = []
uas = []
tugas = []
akhir = []
while lanjut == 'ya':
    na = str(input('Nama\t\t: '))
    ni = int(input('NIM\t\t\t: '))
    tug = int(input('Nilai tugas\t: '))
    ut = int(input('Nilai UTS\t: '))
    us = int(input('nilai uas\t: '))
    akh = float(tug * 0.3) + (ut * 0.35) + (us * 0.35)
    tugas.append(tug)
    nama.append(na)
    nim.append(ni)
    uts.append(ut)
    uas.append(us)
    akhir.append(akh)
    no += 1
    lanjut = input('Tambah data (ya/tidak)? ')


print('========================================================')
print('|NO |   Nama    |    NIM    |Tugas| UTS | UAS | Akhir |')
print('========================================================')
for i in range(no):
    print('|', i + 1, '|  ', nama[i], '   |', nim[i], '|', tugas[i], ' | '
          , uts[i], '| ', uas[i], '|', round(akhir[i], 2), '|')
print('========================================================')















