import sys
import pyinputplus as pypi

def show(Dict, printFormat, title="\ndaftar profil dalam yellow pages:\n"):
    print(title)
    for value in Dict.values():
        print(printFormat.format("", *value))

def search():
    inputId = pypi.inputInt(prompt="Input ID Profile: ", lessThan= len(listPages)-1)
    for i, value in enumerate(listPages.values()):
        if inputId in value:
            print("Info Profil Yang Dicari\n")
            print(f"""ID\t\t : {value[0]}
Nama depan\t : {value[1]}
Nama belakang\t : {value[2]}
usia\t\t : {value[3]}
no telpon\t : {value[4]}
Kode pos\t : {value[5]}
Alamat\t\t : {value[6]}\n"""
)
            break
        elif i == len(listPages) - 1:
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
            show(listPages, printFormat)
        if subReport == 2:
            search()
        if subReport == 3:
            main()
        
def delete():
    show(listPages, printFormat)
    index = pypi.inputInt(
        prompt='Masukkan ID profil yang ingin dihapus: ', 
        lessThan=len(listPages) - 1
    )
    confirm = pypi.inputYesNo(prompt='Apakah anda ingin menghapus profil tersebut?(yes/no): ')
    if confirm == "yes":
        for value in listPages.copy().values():
            if index in value:
                del listPages[f'profil{str(value[0])}']

        for key, value in listPages.copy().items():
            if key != 'column' and value[0] > index:
                del listPages[key]
                listPages.update({
                f'profil{str(value[0]-1)}': [
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
        show(listPages, printFormat)  
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
    show(listPages, printFormat)
    indexInput = pypi.inputInt(prompt="Input ID: ", lessThan= len(listPages))
    for i, value in enumerate(listPages.copy().values()):
        if indexInput in value: 
            print("ID profil sudah ada dalam yellow pages!")
            addMenu()
            break
        elif i == len(listPages) - 1:
            nameInput1 = pypi.inputStr(
            prompt="Input nama depan: ",
            applyFunc=lambda x: x.capitalize(),
            blockRegexes=[r"[0-9]"],
            )
            nameInput2 = pypi.inputStr(
            prompt="Input nama belakang: ",
            applyFunc=lambda x: x.capitalize(),
            blockRegexes=[r"[0-9]"],
            )
            ageInput = pypi.inputInt(
            prompt="Input usia: ",
            )
            numbInput = pypi.inputStr(
            prompt="Input nomor telepon: ",
            blockRegexes=[r"[A-z]"],
            )
            zipInput = pypi.inputInt(
            prompt="Input kode pos: ",
            )
            addInput = pypi.inputStr(
            prompt="Input alamat: ",
            applyFunc=lambda x: x.capitalize(),
            blockRegexes=[r"[0-9]"],
            )
            confirm = pypi.inputYesNo(prompt='Apakah anda ingin menambah ID profil tersebut?(yes/no): ')
            if confirm == "yes":
                listPages.update(
                {f"profil{str(indexInput)}": [indexInput, nameInput1, nameInput2, ageInput, numbInput, zipInput, addInput]}
                )
            show(listPages, printFormat)
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
    indexInput = pypi.inputInt(prompt="Input ID: ", lessThan= len(listPages)-1)
    for i, value in enumerate(listPages.copy().values()):
        if indexInput in value: 

            print("Info Profil\n")
            print(f"""ID\t\t : {value[0]}
Nama depan\t : {value[1]}
Nama belakang\t : {value[2]}
usia\t\t : {value[3]}
no telpon\t : {value[4]}
Kode pos\t : {value[5]}
Alamat\t\t : {value[6]}\n"""
)
            confirm = pypi.inputYesNo(prompt='Apakah anda ingin memperbarui ID profil tersebut?(yes/no): ')
            if confirm == "yes":
                nameInput1 = pypi.inputStr(
                prompt="Input nama depan: ",
                applyFunc=lambda x: x.capitalize(),
                blockRegexes=[r"[0-9]"],
                )
                nameInput2 = pypi.inputStr(
                prompt="Input nama belakang: ",
                applyFunc=lambda x: x.capitalize(),
                blockRegexes=[r"[0-9]"],
                )     
                ageInput = pypi.inputInt(
                prompt="Input usia: ",
                )
                numbInput = pypi.inputStr(
                prompt="Input nomor telepon: ",
                blockRegexes=[r"[A-z]"],
                )
                zipInput = pypi.inputInt(
                prompt="Input kode pos: ",
                )
                addInput = pypi.inputStr(
                prompt="Input alamat: ",
                applyFunc=lambda x: x.capitalize(),
                blockRegexes=[r"[0-9]"],
                )
            if confirm == "no":
                updateMenu() 
            confirm = pypi.inputYesNo(prompt='Apakah anda ingin menyimpan update ID profil tersebut?(yes/no): ')
            if confirm == "yes":
                listPages[f"profil{str(indexInput)}"][1] = nameInput1
                listPages[f"profil{str(indexInput)}"][2] = nameInput2
                listPages[f"profil{str(indexInput)}"][3] = ageInput
                listPages[f"profil{str(indexInput)}"][4] = numbInput
                listPages[f"profil{str(indexInput)}"][5] = zipInput
                listPages[f"profil{str(indexInput)}"][6] = addInput
                show(listPages, printFormat)
            if confirm == "no":
                updateMenu() 
            break
        elif i == len(listPages) - 1:
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
            sys.exit()

if __name__ == "__main__":
    listPages = {
        'column': ["ID", "Nama depan", "nama belakang", "Umur", "No telpon", "Kode pos", "Alamat"],
        'profil0': [0, "Adi", "Satu", 20, "081001", 333333, "depok,sleman"],
        'profil1': [1, "Budi", "Dua", 25, "081002", 444444, "turi,sleman"],
        'profil2': [2, "Citra", "Tiga", 15, "081003", 555555, "kotagede,yogyakarta"],
    }
    
    printFormat = "{:<4}" + "{:<15}" * (len(listPages['column']))
    main()
