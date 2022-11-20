#MENU UTAMA
def mainmenu() :
    print('''+===============================================+
|                                               |
|\tSELAMAT DATANG DI TOKO KOMPUTER OJON\t|
|                                               |
+===============================================+
Menu Aplikasi :
1. Tambah Transaksi
2. Ubah Transaksi
3. Hapus Transaksi
4. Cetak Transaksi
5. Keluar Aplikasi''')
    opsi = int(input('Masukkan Menu: '))
    print("===============================================")
    return opsi


#MENU TAMBAH TRANSAKSI
def tambahdata(data):
    print('''+***************************+
|\tTAMBAH TRANSAKSI    |
+***************************+
Menu Aplikasi :
1. Tambah Transaksi
2. Kembali Ke Menu Utama
''')
    penambahan=dict()
    opsi = int(input('Masukkan Menu: '))
    print("===============================================")
    if opsi == 1:
        keyadd = input('Masukkan Kode Transaksi: ').upper()
        if keyadd in list(data.keys()):
            print('Maaf, Kode Transaksi Sudah Ada!')
        else:
            NAMA = input('Masukkan Nama Barang: ').upper()
            SERI = input('Masukkan Seri Barang: ').upper()
            HARGA = int(input('Masukkan Harga Barang: '))
            JUMLAH = int(input('Masukkan Jumlah Barang: '))
            TOTAL = HARGA * JUMLAH

            accinput = input('Apakah Anda Yakin Akan Menyimpan Data ? <Y/N> : ').upper()
            if accinput == 'Y':
                penambahan={keyadd:{'NAMA':NAMA,'SERI':SERI,'HARGA':HARGA,'JUMLAH':JUMLAH,'TOTAL':TOTAL}}
                print('Data Berhasil Disimpan!')
            else :
                print('Data Gagal Disimpan!')     
    return opsi, penambahan

#FUNGSI CETAK DATA CARD
def printdatacard(data,kunci):
    print(kunci)
    print('*******')
    for key, value in data[kunci].items():
        print(f'\t{key} : {value}')

#MENU UBAH TRANSAKSI
def ubahdata(data):
    print('''+***************************+
|\tUBAH TRANSAKSI    |
+***************************+
Menu Aplikasi :
1. Ubah Transaksi
2. Kembali Ke Menu Utama
''')
    databaru = data
    opsi = int(input('Masukkan Menu: '))
    print("===============================================")
    if opsi == 1:
        keyedit = input('Masukkan Kode Transaksi: ').upper()
        if keyedit not in list(data.keys()):
            print('Maaf, Kode Transaksi Tidak Ada!')
        else:
            printdatacard(data,keyedit)
            print("=================")
            
            accedit = input('Apakah Anda Yakin Akan Mengubah Data ? <Y/N> : ').upper()
            if accedit == 'Y':
                NAMA = input('Masukkan Nama Barang: ').upper()
                if NAMA == '':
                    NAMA = data[keyedit]['NAMA']
                SERI = input('Masukkan Seri Barang: ').upper()
                if SERI == '':
                    SERI = data[keyedit]['SERI']
                HARGA = input('Masukkan Harga Barang: ')
                if HARGA == '':
                    HARGA = data[keyedit]['HARGA']
                else :
                    HARGA = int(HARGA)
                JUMLAH = input('Masukkan Jumlah Barang: ')
                if JUMLAH == '':
                    JUMLAH = data[keyedit]['JUMLAH']
                else :
                    JUMLAH = int(JUMLAH)
                TOTAL = HARGA * JUMLAH
                acceditfinal = input('Apakah Anda Yakin Akan Menyimpan Data Yang Diubah ? <Y/N> : ').upper()
                if acceditfinal == 'Y':
                    data[keyedit]={'NAMA':NAMA,'SERI':SERI,'HARGA':HARGA,'JUMLAH':JUMLAH,'TOTAL':TOTAL}
                    print('Data Berhasil Diubah!')
            else :
                print('Data Gagal Diubah!')              
    
    return opsi, databaru

#MENU HAPUS TRANSAKSI
def hapusdata(data):
    print('''+***************************+
|\tHAPUS TRANSAKSI    |
+***************************+
Menu Aplikasi :
1. Hapus Transaksi
2. Kembali Ke Menu Utama
''')
    databaru = data
    opsi = int(input('Masukkan Menu: '))
    print("===============================================")
    if opsi == 1:
        keydel = input('Masukkan Kode Transaksi: ').upper()
        if keydel not in list(data.keys()):
            print('Maaf, Kode Transaksi Tidak Ada!')
        else:
            printdatacard(data,keydel)
            print("=================")
            
            accdel = input('Apakah Anda Yakin Akan Menghapus Data ? <Y/N> : ').upper()
            if accdel == 'Y':
                del databaru[keydel]
                print('Data Berhasil Dihapus!')
            else :
                print('Data Gagal Dihapus!')     
    return opsi, databaru

#MENU CETAK TRANSAKSI
def cetakdata(data):
    print('''+***************************+
|\tCETAK TRANSAKSI    |
+***************************+
Menu Aplikasi :
1. Cetak Semua Transaksi
2. Cetak Transaksi Sesuai ID Transaksi
3. Kembali Ke Menu Utama
''')
    opsi = int(input('Masukkan Menu: '))
    print("===============================================")
    if opsi == 1:
        for key,value in data.items():
            printdatacard(data,key)
    elif opsi == 2:
        readkey = input('Masukkan Kode Transaksi: ').upper()
        if readkey in list(data.keys()) :
            printdatacard(data,readkey)
        else:
            print('Data Tidak Ditemukan!')
           
    return opsi


#BAGIAN UTAMA APLIKASI
dataset = {'TR-1':{'NAMA':'PC','SERI':'LENOVO LITE','HARGA':1000000,'JUMLAH':20,'TOTAL':200000}}
tuasprogram = True

while tuasprogram :
    menu = mainmenu()
    tuasmenu = True

    if menu == 1:
        while tuasmenu :
            submenu = tambahdata(dataset)
            if submenu[0] == 1:
                dataset.update(submenu[1])
            if submenu[0] == 2:
                keluar = input('Apakah Anda Kembali Ke Menu Utama ? <Y/N> : ')
                if keluar == 'Y' or keluar == 'y':
                    tuasmenu = False
            input("_______________")
                
    elif menu == 2:
        while tuasmenu :
            submenu = ubahdata(dataset)
            if submenu[0] == 1:
                dataset = submenu[1]
            if submenu[0] == 2:
                keluar = input('Apakah Anda Kembali Ke Menu Utama ? <Y/N> : ')
                if keluar == 'Y' or keluar == 'y':
                    tuasmenu = False
            input("_______________")

    elif menu == 3:
        while tuasmenu :
            submenu = hapusdata(dataset)
            if submenu[0] == 1:
                dataset = submenu[1]
            if submenu[0] == 2:
                keluar = input('Apakah Anda Kembali Ke Menu Utama ? <Y/N> : ')
                if keluar == 'Y' or keluar == 'y':
                    tuasmenu = False
            input("_______________")

    elif menu == 4:
        while tuasmenu :
            submenu = cetakdata(dataset)
            if submenu == 3:
                keluar = input('Apakah Anda Kembali Ke Menu Utama ? <Y/N> : ')
                if keluar == 'Y' or keluar == 'y':
                    tuasmenu = False
            input("_______________")

    elif menu == 5:
        keluar = input('Apakah Anda Yakin Akan Menyudahi Program ? <Y/N> : ').upper()
        if keluar == 'Y' :
            tuasprogram = False
        
    else :
        print('Maaf, Menu yang Anda Masukkan Salah. Silahkan Pilih Menu Kembali!')
        input("_______________")
    
    

print('Program Telah Selesai, Terima Kasih!')
    

    
