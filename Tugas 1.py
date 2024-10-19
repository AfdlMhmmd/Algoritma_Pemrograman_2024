# program mengecek ipk dan menentukan kelulusan 
def ulng():
    print(lgn ,"Ngulang satu semester lagi ya...")
    
def lls():
    print(f"Selamat {lgn} kamu dinyatakan lulus!")
    print("Kami tunggu kamu di acara wisuda nanti ya!")

def ggl():
    print("Masukan angka yang benar")
    
lgn = ""
nim = ""
prodi = ""
    
def ipk():
        print("Silahkan masukan dengan benar")
        ujian = int(input("Masukan nilai ujian (0-100): "))
        uts = int(input("Masukan nilai UTS (0-100): "))
        uas = int(input("Masukan nilai UAS (0-100): "))

        if 0 <= ujian <= 100 and 0 <= uts <= 100 and 0 <= uas <= 100:
            if ujian >= 90 and uts >= 90 and uas >= 90:
                print("Nilai IPK anda 4,00.")
            elif ujian >= 85 and uts >= 85 and uas >= 85:
                print("Nilai IPK anda 3,50.")
            elif ujian >= 80 and uts >= 80 and uas >= 80:
                print("Nilai IPK anda 3,00.")
            elif ujian >= 75 and uts >= 75 and uas >= 75:
                print("Nilai IPK anda 2,50.")
            elif ujian <= 75 and uts <= 75 and uas <= 75:
                print("Nilai IPK anda 2,00.")
            else:
                ggl()
        else:
            print("Nilai yang dimasukan antara 0 dan 100!")
        
        menu()

def penentu():
    penentu = input("Masukan Nilai IPK anda: ")
    
    
    if penentu == "4,00":
        lls()
        menu()
    
    elif penentu == "3,50":
        lls()
        menu()
    
    elif penentu == "3,00":
        lls()
        menu()
        
    elif penentu == "2,50":
        lls()
        menu()
    
    elif  penentu == "2,00":
        ulng()
        menu()
    else:
        ggl()
        
def biodata():
    global lgn, nim, prodi
    print("BIODATA MAHASISWA")
    print("Nama  :", lgn)
    print("Nim   :", nim)
    print("Prodi :", prodi)
        
def login_utama():
    global lgn, nim, prodi
    lgn = input("Masukan nama kamu: ")
    nim = input("Masukan NIM kamu: ")
    prodi = input("Masukan Prodi kamu: ")
    menu()
        
def menu():        
    while True:
        print(f"||======Selamat datang {lgn}=====||")
        print("Menu")
        print("1. CEK IPK")
        print("2. CEK KELULUSAN")
        print("3. BIODATA MAHASISWA")
        print("4. KELUAR")

        masukan = int(input("Masukan Pilihan (1/2/3/4): "))
        if masukan == 1:
            ipk()
        elif masukan == 2:
            penentu()
        elif masukan == 3:
            biodata()
        elif masukan == 4:
            print("Anda keluar dari program!")
            break
        else:
            ggl()
            
login_utama()





                            
                           