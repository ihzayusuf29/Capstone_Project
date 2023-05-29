import sys
import pyinputplus as pypi
import csv

def show(Dict, printFormat, title="\ndaftar profil dalam yellow pages:\n"):
    print(title)
    for value in Dict.values():
        #BUG
        print(printFormat.format("", *value))

def search():
    inputId = pypi.inputInt(prompt="Input ID Profile: ", lessThan= len(dataProfil)-1)
    for i, value in enumerate(dataProfil.values()):
        if inputId in value:
            print("Info Profil Yang Dicari\n")
            print(f"""ID\t\t : {value[0]}
Nama Perusahaan\t : {value[1]}
Alamat E-mail\t : {value[2]}
Sektor Bisnis\t : {value[3]}
No Telpon\t : {value[4]}
Kode Pos\t : {value[5]}
Alamat\t\t : {value[6]}\n"""
)
            break
        elif i == len(dataProfil) - 1:
            print(f"Profil dengan {inputId} tidak dapat ditemukan")
            reportMenu()

def reportMenu():
    while True:
        print('''
Menu Show Yellow Pages:
1. Show all profile on yellow pages
2. Search yellow pages profile
3. Back to main menu \n
            ''')
        subReport = pypi.inputInt(prompt="Input menu number [1-3]: ", lessThan= 4)
        if subReport == 1:
            show(dataProfil, printFormat)
        if subReport == 2:
            search()
        if subReport == 3:
            main()
        
def delete():
    show(dataProfil, printFormat)
    index = pypi.inputInt(
        prompt='Masukkan ID profil yang ingin dihapus: ', 
        lessThan=len(dataProfil) - 1
    )
    confirm = pypi.inputYesNo(prompt='Apakah anda ingin menghapus profil tersebut?(yes/no): ')
    if confirm == "yes":
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
        print("data berhasil dihapus")
        show(dataProfil, printFormat)  
    if confirm == "no":
        deleteMenu   

def deleteMenu():
    while True:
        print('''
Menu Menghapus profil Yellow Pages:
1. Delete yellow pages profile
2. Back to main menu \n
            ''')
        subReport = pypi.inputInt(prompt="Input menu number [1-2]: ", lessThan= 3)
        if subReport == 1:
            delete()
        if subReport == 2:
            main()

def add():
    show(dataProfil, printFormat)
    indexInput = pypi.inputInt(prompt="Input ID: ", lessThan= len(dataProfil))
    for i, value in enumerate(dataProfil.copy().values()):
        if indexInput in value: 
            print("ID profil sudah ada dalam yellow pages!")
            addMenu()
            break
        elif i == len(dataProfil) - 1:
            nameInput1 = pypi.inputStr(
            prompt="Input nama perusahaan: ",
            applyFunc=lambda x: x.capitalize()
            ,blockRegexes=[r"[0-9]"]
            ),
            emailInput = pypi.inputStr(
            prompt="Input alamat e-mail: ",
            applyFunc=lambda x: x.capitalize()
            ),
            sectorInput = pypi.inputStr(
            prompt="Input sektor bisnis: ",
            applyFunc=lambda x: x.capitalize()
            ),
            numbInput = pypi.inputStr(
            prompt="Input nomor telepon: ",
            blockRegexes=[r"[A-z]"],
            ),
            zipInput = pypi.inputInt(
            prompt="Input kode pos: ",
            ),
            addInput = pypi.inputStr(
            prompt="Input alamat: ",
            applyFunc=lambda x: x.capitalize(),
            blockRegexes=[r"[0-9]"],
            )
            confirm = pypi.inputYesNo(prompt='Apakah anda ingin menambah ID profil tersebut?(yes/no): ')
            if confirm == "yes":
                dataProfil.update(
                {f"profil{indexInput}" : [
                    indexInput, nameInput1, emailInput, sectorInput, numbInput, zipInput, addInput]}
                )
            show(dataProfil, printFormat)
            if confirm == "no":
                addMenu()

def addMenu():
    while True:
        print('''
Menu Menambah profil Yellow Pages Baru:
1. Add new yellow pages profile
2. Back to main menu \n
            ''')
        subReport = pypi.inputInt(prompt="Input menu number [1-2]: ", lessThan= 3)
        if subReport == 1:
            add()
        if subReport == 2:
            main()
      
def update():
    indexInput = pypi.inputInt(prompt="Input ID: ", lessThan= len(dataProfil)-1)
    for i, value in enumerate(dataProfil.copy().values()):
        if indexInput in value: 

            print("Info Profil\n")
            print(f"""ID\t\t : {value[0]}
Nama perusahaan\t : {value[1]}
Alamat E-Mail\t : {value[2]}
Sektor Bisnis\t : {value[3]}
no telpon\t : {value[4]}
Kode pos\t : {value[5]}
Alamat\t\t : {value[6]}\n"""
)
            confirm = pypi.inputYesNo(prompt='Apakah anda ingin memperbarui ID profil tersebut?(yes/no): ')
            if confirm == "yes":
                nameInput1 = pypi.inputStr(
                prompt="Input nama perusahaan: ",
                applyFunc=lambda x: x.capitalize(),
                blockRegexes=[r"[0-9]"],
                )
                emailInput = pypi.inputStr(
                prompt="Input alamat e-mail: ",
                applyFunc=lambda x: x.capitalize()
                ),
                sectorInput = pypi.inputStr(
                prompt="Input sektor bisnis: ",
                applyFunc=lambda x: x.capitalize()
                ),
                numbInput = pypi.inputStr(
                prompt="Input nomor telepon: ",
                blockRegexes=[r"[A-z]"]
                ),
                zipInput = pypi.inputInt(
                prompt="Input kode pos: "
                ),
                addInput = pypi.inputStr(
                prompt="Input alamat: ",
                applyFunc=lambda x: x.capitalize(),
                blockRegexes=[r"[0-9]"]
                )
            if confirm == "no":
                updateMenu() 
            confirm = pypi.inputYesNo(prompt='Apakah anda ingin menyimpan update ID profil tersebut?(yes/no): ')
            if confirm == "yes":
                dataProfil[f"profil{indexInput}"][1] = nameInput1
                dataProfil[f"profil{indexInput}"][2] = emailInput
                dataProfil[f"profil{indexInput}"][3] = sectorInput
                dataProfil[f"profil{indexInput}"][4] = numbInput
                dataProfil[f"profil{indexInput}"][5] = zipInput
                dataProfil[f"profil{indexInput}"][6] = addInput
            show(dataProfil, printFormat)
            if confirm == "no":
                updateMenu() 
            break
        elif i == len(dataProfil) - 1:
            print("profil tidak ada dalam yellow pages!")
            updateMenu()

def updateMenu():
 while True:
        print('''
Menu Update profile Yellow Pages:
1. Update Existing yellow pages profile
2. Back to main menu \n
            ''')
        subReport = pypi.inputInt(prompt="Input menu number [1-2]: ", lessThan= 3)
        if subReport == 1:
            update()
        if subReport == 2:
            main()    

def main():
    while True:
        prompt = f"Welcome to Yellow Pages App!\nList menu:\n\n"
        choice = ['Show', 'Add', 'Delete', 'Update', 'Exit']
        response = pypi.inputMenu(prompt=prompt, choices=choice, numbered=True)

        if response == 'Show':
            reportMenu()
        elif response == 'Add':
            addMenu()
        elif response == 'Delete':
            deleteMenu()
        elif response == 'Update':
            updateMenu()
        else:
            print("Terimakasih telah menggunakan Yellow Pages app!")
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

    printFormat = "{:<4}" + "{:<15}" * (len(dataProfil['column']))
    
    main()
