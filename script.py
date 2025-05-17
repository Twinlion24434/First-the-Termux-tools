import os

def menu():
    print("TwinLion Tool")
    print("1. Update dan upgrade package")
    print("2. Install Python dan pip")
    print("3. Install dependencies lainnya")
    print("4. Keluar")

def main():
    while True:
        menu()
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            os.system("pkg update && pkg upgrade -y")
        elif pilihan == "2":
            os.system("pkg install python -y && pkg install python-pip -y")
        elif pilihan == "3":
            os.system("pkg install git -y")
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
