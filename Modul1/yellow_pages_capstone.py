import sys
import pyinputplus as pypi
import csv
import tabulate

#fungsi menampilkan semua profil dalam database
def show(dataProfil, title= '\nDaftar profil dalam yellow pages:\n'):
    if len(dataProfil) <=1  or 'column' not in dataProfil.keys():
        print('Data profil yellow pages kosong')
    else:    
        print(title)
        data = list(dataProfil.values())[1:]
        header = dataProfil['column']
        print(tabulate.tabulate(data, header, tablefmt='outline'))
        print('\n')

#fungsi mencari database berdasarkan indeks
def search():
    inputId = pypi.inputInt(
        prompt = 'Masukkan ID Profil: ', 
        lessThan = len(dataProfil)-1, 
        blockRegexes = '-')
    for i, value in enumerate(dataProfil.values()):
        if inputId in value:
            print('Info Profil Yang Dicari\n')
            print(f"""ID\t\t : {value[0]}
Nama Perusahaan\t : {value[1]}
Alamat Email\t : {value[2]}
Sektor Bisnis\t : {value[3]}
No Telpon\t : {value[4]}
Kode Pos\t : {value[5]}
Alamat\t\t : {value[6]}\n"""
)
            break
        elif i == len(dataProfil) - 1:
            print(f'Profil dengan {inputId} tidak dapat ditemukan')
            reportMenu()

#Fungsi menampilkan submenu show
def reportMenu():
    while True:
        print('''
Menu Show Yellow Pages:
1. Menampilkan semua profil yellow pages
2. Mencari profil yellow pages
3. Kembali ke menu utama \n
            ''')
        subReport = pypi.inputInt(prompt= 'Masukkan nomor menu [1-3]: ', lessThan= 4)
        if subReport == 1:
            show(dataProfil)
        if subReport == 2:
            search()
        if subReport == 3:
            main()

#Fungsi menghapus profil dalam database        
def delete():
    show(dataProfil)
    index = pypi.inputInt(
        prompt='Masukkan ID profil yang ingin dihapus: ', 
        lessThan= len(dataProfil) - 1, blockRegexes= '-'
    )
    confirm = pypi.inputYesNo(prompt= 'Apakah anda ingin menghapus profil tersebut?(yes/no): ')
    if confirm == 'yes':
        for value in dataProfil.copy().values():
            if index in value:
                del dataProfil[f'profil{str(value[0])}']

        for key, value in dataProfil.copy().items():
            if key != 'column' and value[0] > index:
                del dataProfil[key]
                dataProfil.update({
                f'profil{(value[0]-1)}': [
                    value[0]-1, 
                    value[1], 
                    value[2], 
                    value[3],
                    value[4],
                    value[5],
                    value[6]]
                }
            )
        print('data berhasil dihapus')
        show(dataProfil)  
    if confirm == 'no':
        deleteMenu   

#Fungsi menampilkan submenu delete
def deleteMenu():
    while True:
        print('''
Menu Menghapus profil Yellow Pages:
1. Hapus profil yellow pages
2. Kembali ke menu utama \n
            ''')
        subDelete = pypi.inputInt(prompt= 'Masukkan nomor menu [1-2]: ', lessThan= 3)
        if subDelete == 1:
            delete()
        if subDelete == 2:
            main()

#Fungsi menambah profil baru kedalam database
def add():
    show(dataProfil)
    indexInput = pypi.inputInt(
        prompt= 'Masukkan ID: ', 
        lessThan= len(dataProfil),
        blockRegexes= '-')
    for i, value in enumerate(dataProfil.copy().values()):
        if indexInput in value: 
            print('ID profil sudah ada dalam yellow pages!')
            add()
            break
        elif i == len(dataProfil) - 1:
            nameInput1 = pypi.inputStr(
            prompt = 'Masukkan nama perusahaan: ',
            applyFunc = lambda x: x.capitalize(),
            blockRegexes = [r'[0-9]']
            )
            emailInput = pypi.inputStr(
            prompt = 'Masukkan alamat e-mail: ',
            applyFunc = lambda x: x.capitalize()
            )
            sectorInput = pypi.inputStr(
            prompt = 'Masukkan sektor bisnis: ',
            applyFunc = lambda x: x.capitalize(),
            blockRegexes = [r'[0-9]']
            )
            numbInput = pypi.inputStr(
            prompt = 'Masukkan nomor telepon: ',
            blockRegexes = [r'[A-z]']
            )
            zipInput = pypi.inputInt(
            prompt = 'Masukkan kode pos: '
            )
            addInput = pypi.inputStr(
            prompt = 'Masukkan alamat: ',
            applyFunc = lambda x: x.capitalize(),
            blockRegexes = [r'[@#$]']
            )
            confirm = pypi.inputYesNo(prompt='Apakah anda ingin menambah ID profil tersebut?(yes/no): ')
            if confirm == 'yes':
                dataProfil.update(
                {f'profil{indexInput}' : [
                    indexInput, nameInput1, emailInput, sectorInput, numbInput, zipInput, addInput]}
                )
            show(dataProfil)
            if confirm == 'no':
                addMenu()

#Fungsi menampilkan submenu add
def addMenu():
    while True:
        print('''
Menu Menambah profil Yellow Pages Baru:
1. Menambah Profil Baru
2. Kembali ke menu utama \n
            ''')
        subAdd = pypi.inputInt(prompt= 'Masukkan nomor menu [1-2]: ', lessThan= 3)
        if subAdd == 1:
            add()
        if subAdd == 2:
            main()

#Fungsi memperbarui database    
def update():
    indexInput = pypi.inputInt(prompt= 'Masukkan ID: ', lessThan= len(dataProfil)-1, blockRegexes= '-')
    for i, value in enumerate(dataProfil.copy().values()):
        if indexInput in value: 

            print('Info Profil\n')
            print(f"""ID\t\t : {value[0]}
Nama perusahaan\t : {value[1]}
Alamat E-Mail\t : {value[2]}
Sektor Bisnis\t : {value[3]}
no telpon\t : {value[4]}
Kode pos\t : {value[5]}
Alamat\t\t : {value[6]}\n"""
)
            confirm = pypi.inputYesNo(prompt='Apakah anda ingin memperbarui ID profil tersebut?(yes/no): ')
            if confirm == 'yes':
                nameInput1 = pypi.inputStr(
                prompt = 'Masukkan nama perusahaan: ',
                applyFunc = lambda x: x.capitalize(),
                blockRegexes = [r'[0-9]'],
                )
                emailInput = pypi.inputStr(
                prompt = 'Masukkan alamat email: ',
                applyFunc = lambda x: x.capitalize(),
                allowRegexes = [r'[A-Za-z0-9/_/./@]']
                )
                sectorInput = pypi.inputStr(
                prompt = 'Masukkan sektor bisnis: ',
                applyFunc = lambda x: x.capitalize()
                )
                numbInput = pypi.inputStr(
                prompt = 'Masukkan nomor telepon: ',
                blockRegexes = [r"[A-z]"]
                )
                zipInput = pypi.inputInt(
                prompt = 'Masukkan kode pos: '
                )
                addInput = pypi.inputStr(
                prompt = 'Masukkan alamat: ',
                applyFunc = lambda x: x.capitalize(),
                blockRegexes = ['!','@','%','_','-']
                )
            if confirm == 'no':
                updateMenu() 
            confirm = pypi.inputYesNo(prompt='Apakah anda ingin menyimpan update ID profil tersebut?(yes/no): ')
            if confirm == 'yes':
                dataProfil[f'profil{indexInput}'][1] = nameInput1
                dataProfil[f'profil{indexInput}'][2] = emailInput
                dataProfil[f'profil{indexInput}'][3] = sectorInput
                dataProfil[f'profil{indexInput}'][4] = numbInput
                dataProfil[f'profil{indexInput}'][5] = zipInput
                dataProfil[f'profil{indexInput}'][6] = addInput
            show(dataProfil)
            if confirm == 'no':
                updateMenu() 
            break
        elif i == len(dataProfil) - 1:
            print('Profil tidak ada dalam yellow pages!')
            updateMenu()

#Fungsi menampilkan submenu update
def updateMenu():
 while True:
        print('''
Menu Update profile Yellow Pages:
1. Update profil yellow pages
2. Kembali ke menu utama \n
            ''')
        subUpdate = pypi.inputInt(prompt= 'Masukkan nomor menu [1-2]: ', lessThan= 3)
        if subUpdate == 1:
            update()
        if subUpdate == 2:
            main()    

#Fungsi tampilan awal
def main():
    while True:
        prompt = f'Welcome to Yellow Pages App!\nList menu:\n\n'
        choice = ['Show', 'Add', 'Delete', 'Update', 'Exit']
        response = pypi.inputMenu(prompt= prompt, choices= choice, numbered= True)

        if response == 'Show':
            reportMenu()
        elif response == 'Add':
            addMenu()
        elif response == 'Delete':
            deleteMenu()
        elif response == 'Update':
            updateMenu()
        else:
            print('Terimakasih telah menggunakan Yellow Pages app!')
            #Export data ke csv
            fileDataProfil = open(pathProfil, 'w', newline='')
            writerDataProfil = csv.writer(fileDataProfil, delimiter= ';')
            writerDataProfil.writerows(dataProfil.values())
            fileDataProfil.close()
            #Exit apps
            sys.exit()

if __name__ == "__main__":
    #Import database profil dari file csv
    pathProfil = 'C:/Users/Ihza/Documents/Capstone_Project/Modul1/Data_Profil.csv'

    fileDataProfil = open(pathProfil)
    readerDataProfil = csv.reader(fileDataProfil, delimiter= ';')
    headingsDataProfil = next(readerDataProfil)

    dataProfil = {'column': headingsDataProfil}
    for row in readerDataProfil:
        dataProfil.update(
            {
                str(f'profil{row[0]}') :
                [int(row[0]),
                 str(row[1]),
                 str(row[2]),
                 str(row[3]),
                 int(row[4]),
                 str(row[5]),
                 str(row[6])
                 ]

            }
        )
    
    main()

#tabulate ada char aneh sebelum id
#csv tidak bisa diawali dengan 0 (nomor telp)
#fungsi block/allow regexes tidak berfungsi
