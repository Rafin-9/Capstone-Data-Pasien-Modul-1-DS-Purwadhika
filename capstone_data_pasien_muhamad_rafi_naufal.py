import regex as re
from tabulate import tabulate as tb

# List untuk menyimpan data pasien yang sudah pulang
pasien_pulang = []

data_pasien = [
    {'Nomor_Pasien': '101', 'Nama': 'Arya', 'Usia': 25, 'Gender': 'M', 'NIK': '3374111904000019', 'BPJS': 'Tidak memakai BPJS', 'Pembayaran': 'Lunas'},
    {'Nomor_Pasien': '102', 'Nama': 'Reza', 'Usia': 30, 'Gender': 'M', 'NIK': '3374112109000005', 'BPJS': 'Tidak memakai BPJS', 'Pembayaran': 'Belum'},
    {'Nomor_Pasien': '103', 'Nama': 'Refli', 'Usia': 34, 'Gender': 'M', 'NIK': '3374111308000022', 'BPJS': 'Tidak memakai BPJS', 'Pembayaran': 'Belum'},
    {'Nomor_Pasien': '104', 'Nama': 'Handoyo', 'Usia': 36, 'Gender': 'M', 'NIK': '3374111208000015', 'BPJS': 'Memakai BPJS', 'Pembayaran': 'Lunas'},
    {'Nomor_Pasien': '105', 'Nama': 'Dandy', 'Usia': 38, 'Gender': 'M', 'NIK': '3374111617000007', 'BPJS': 'Memakai BPJS', 'Pembayaran': 'Lunas'},
    {'Nomor_Pasien': '106', 'Nama': 'Faruq', 'Usia': 29, 'Gender': 'M', 'NIK': '3374111812000102', 'BPJS': 'Memakai BPJS', 'Pembayaran': 'Belum'},
    {'Nomor_Pasien': '107', 'Nama': 'Hisyam', 'Usia': 27, 'Gender': 'M', 'NIK': '3374111718000008', 'BPJS': 'Memakai BPJS', 'Pembayaran': 'Lunas'},
    {'Nomor_Pasien': '108', 'Nama': 'Gilang', 'Usia': 26, 'Gender': 'M', 'NIK': '3374111520000012', 'BPJS': 'Tidak memakai BPJS', 'Pembayaran': 'Lunas'},
    {'Nomor_Pasien': '109', 'Nama': 'Alwan', 'Usia': 27, 'Gender': 'M', 'NIK': '3374111904000004', 'BPJS': 'Tidak memakai BPJS', 'Pembayaran': 'Belum'}
]

def mengecek_nama(nama):
    mengecek_nama_replace = nama.replace(' ', '')
    return mengecek_nama_replace.isalpha()

def mengecek_usia(data_pasien, usia):
    if re.match(r'\d{1,3}', usia): # Memastikan usia adalah angka dan berjumlah 3 digit
        usia_int = int(usia) # Konversi usia ke integer
        if 1 <= usia_int <= 120:
            print('Input usia harus menggunakan angka dan maksimal berjumlah 3 digit.')
            return False # Usia valid
        else:
            print('Usia harus diantara 1 dan 120.')
            return True  # Usia tidak valid
    else:
        print('Input usia harus menggunakan angka dan maksimal 3 digit')
        return True # Usia tidak valid

def mengecek_nomor_NIK(data_pasien, NIK):
    if re.fullmatch(r'\d{16}', NIK):
        print('Input NIK anda berjumlah 16 digit.')
        return True
    else:
        print('Input NIK harus menggunakan angka dan berjumlah 16 digit.')
        return False  # NIK tidak valid

def duplikat_NIK(data_pasien, NIK):
    for search in data_pasien:
        if search['NIK'] == NIK:
            return True  # NIK sudah ada
    return False  # NIK tidak ada dalam data


def duplikat_Nomor_Pasien(data_pasien, Nomor_Pasien):
    return any(pasien['Nomor_Pasien'] == Nomor_Pasien for pasien in data_pasien)

def mencari_data_pasien(data_pasien, nama):
    pasien_found = next((pasien for pasien in data_pasien if pasien['Nama'].lower() == nama.lower()), None)
    if pasien_found:
        print("Data pasien ditemukan:")
        print(tb([pasien_found], headers='keys', tablefmt='github'))
    else:
        print("Pasien tidak ditemukan. Silakan coba lagi.")

def urutan_data_usia(data_pasien):
    return sorted(data_pasien, key=lambda pasien: pasien['Usia'])

def show_list(data_pasien):
    if not data_pasien:
        print('Pasien tidak ada.')
    else:
        print(tb(data_pasien, headers='keys', tablefmt='github'))

def menu_1():
    while True:
        print("\n1. Data Pasien di Rumah Sakit\n2. Pasien yang menggunakan BPJS\n3. Pasien yang tidak menggunakan BPJS\n4. Urutan Pasien dari termuda\n5. Mencari Nama Pasien \n6. Back to Main Menu")
        menu1_confirmation = input("Enter your choice: ")
        if menu1_confirmation == '1':
            show_list(data_pasien)
        elif menu1_confirmation in ['2', '3']: # Filter untuk pengguna BPJS dan tidak
            bpjs_status = 'Memakai BPJS' if menu1_confirmation == '2' else 'Tidak memakai BPJS'
            filtered_pasien = [pasien for pasien in data_pasien if pasien['BPJS'] == bpjs_status]
            if filtered_pasien:
                print(f"\nData Pasien yang {bpjs_status}: ")
                print(tb(filtered_pasien, headers='keys', tablefmt='github'))
            else:
                print(f"Tidak ada pasien yang {bpjs_status}.")
        elif menu1_confirmation == '4': # Sort berdasarkan dari usia termuda
            sorted_pasien = urutan_data_usia(data_pasien)
            print("\nData Pasien dari termuda:")
            print(tb(sorted_pasien, headers='keys', tablefmt='github'))
        elif menu1_confirmation == '5': # Search pasien
            nama_cari = input("Masukkan nama pasien yang dicari: ").strip()
            if nama_cari:
                pasien_found = mencari_data_pasien(data_pasien, nama_cari)
            if pasien_found:
                print(f"\nData Pasien yang dicari {nama_cari.title()}")
                print(tb(mencari_data_pasien, headers='keys', tablefmt='github'))
            else:
                print("Pasien tidak ditemukan. Silakan coba lagi.")
        elif menu1_confirmation == '6':
            return  # Back to main menu
        else:
            print("Invalid input. Please enter '1', '2', '3', '4' or '5'.")

def add_pasien(data_pasien):
    while True:
        print("1. Add Pasien\n2. Back to Main Menu")
        menu2_confirmation = input("Enter your choice: ")
        if menu2_confirmation == '1':
            break
        elif menu2_confirmation == '2':
            return  # Back to main menu
        else:
            print("Invalid input. Please enter '1' or '2'\n")

    while True:
        nama = input("Masukkan nama pasien: ").title()
        if mengecek_nama(nama):
            break
        else:
            print("Nama hanya boleh berisi huruf. Silakan coba lagi.")

    while True:
        gender = input("Masukkan jenis kelamin anda (M/F): ").upper()
        if gender in ['M', 'F']:
            break
        else:
            print("Input tidak valid. Input M atau F saja.")

    while True:
        try:
            usia = (input("Masukkan usia pasien: "))
            if mengecek_usia(data_pasien, usia):
                continue
            else:
                print("Usia Valid.")
                break
        except ValueError:
            print("Input tidak valid. Usia harus berupa angka.")

    while True:
        NIK = input("Masukkan NIK pasien: ")
        if mengecek_nomor_NIK(data_pasien, NIK):
            if duplikat_NIK(data_pasien, NIK):
                print("Nomor NIK anda terdapat duplikasi pada data kami. Silakan masukkan NIK yang berbeda.")
            else:
                print("Nomor NIK anda Valid")
                break
        else:
            print("Nomor NIK anda tidak Valid, silahkan masukan NIK anda kembali (16 digit angka)")

    while True:
        BPJS = input("Apakah pasien akan menggunakan BPJS (Ya/Tidak): ").capitalize()
        if BPJS in ['Ya', 'Tidak']:
            nomor_bpjs = 'Memakai BPJS' if BPJS == 'Ya' else 'Tidak memakai BPJS'
            break
        else:
            print("Input tidak valid. Silakan coba lagi.")

    while True:
        status_pembayaran = input("Masukkan status pembayaran (Lunas/Belum): ").strip().capitalize()
        if status_pembayaran in ['Lunas', 'Belum']:
            status_pembayaran1 = 'Lunas' if status_pembayaran == 'Lunas' else 'Belum'
            break
        else:
            print("Input tidak valid. Silakan coba lagi.")


    new_pasien = {
        'Nomor_Pasien': str(max(int(pasien['Nomor_Pasien'])for pasien in data_pasien)+ 1),
        'Nama': nama,
        'Usia': usia,
        'Gender': gender,
        'NIK': NIK,
        'BPJS': nomor_bpjs,
        'Pembayaran': status_pembayaran
    }

    data_pasien.append(new_pasien)
    print(f"Data pasien {nama} berhasil ditambahkan.\n")

def update_pasien(data_pasien):
    while True:
        print("1. Update Data Pasien\n2. Back to Main Menu")
        menu3_confirmation = input("Enter your choice: ")
        if menu3_confirmation == '1':
            break
        elif menu3_confirmation == '2':
            return  # Back to main menu
        else:
            print("Invalid input. Please enter '1' or '2'\n")

    while True:
        nama = input("Masukkan nama pasien yang ingin diupdate: ").title()
        pasien_found = next((pasien for pasien in data_pasien if pasien['Nama'].lower() == nama.lower()), None)

        if pasien_found:
            print("Data pasien ditemukan:")
            print(tb([pasien_found], headers='keys', tablefmt='github'))
            break
        else:
            print("Pasien tidak ditemukan. Silakan coba lagi.")

    while True:
        field_to_update = input("Masukkan field yang ingin diupdate (Usia/Gender/NIK/BPJS) atau ketik 'Done' untuk selesai: ").title()
        if field_to_update == 'Done':
            break
        elif field_to_update not in ['Usia', 'Gender', 'Nik', 'Bpjs']:
            print("Input tidak valid. Silakan coba lagi.")
            continue

        if field_to_update == 'Usia':
            while True:
                try:
                    usia = input("Masukkan usia baru pasien: ")
                    if not mengecek_usia(data_pasien, usia): # Memanggil fungsi mengecek usia
                        pasien_found['Usia'] = usia
                        print(f"Usia pasien {nama} berhasil diupdate menjadi {usia}.")
                        break
                except ValueError:
                    print("Input tidak valid. Usia harus berupa angka.")

        elif field_to_update == 'Gender':
            while True:
                jenis_kelamin = input("Masukkan jenis kelamin anda (M/F): ").upper()
                if jenis_kelamin in ['M', 'F']:
                    pasien_found['Gender'] = jenis_kelamin
                    print(f"Jenis kelamin pasien {nama} berhasil diupdate menjadi {jenis_kelamin}.")
                    break
                else:
                    print("Input tidak valid. Input M atau F saja.")

        elif field_to_update == 'Nik':
            while True:
                NIK = input("Masukkan NIK baru pasien: ")
                if mengecek_nomor_NIK(data_pasien, NIK):
                    if duplikat_NIK(data_pasien, NIK):
                        print("Nomor NIK anda terdapat duplikasi pada data kami. Silakan masukkan NIK yang berbeda.")
                    else:
                        print("Nomor NIK anda Valid")
                        break
                else:
                    print("Nomor NIK anda tidak Valid, silahkan masukan NIK anda kembali (16 digit angka)")
                    pasien_found['NIK'] = NIK
                    print(f"NIK pasien {nama} berhasil diupdate menjadi {NIK}.")
                    break

        elif field_to_update == 'Bpjs':
            while True:
                bpjs_baru = input("Apakah pasien akan menggunakan BPJS (Ya/Tidak): ").capitalize()
                if bpjs_baru in ['Ya', 'Tidak']:
                    pasien_found['BPJS'] = 'Memakai BPJS' if bpjs_baru == 'Ya' else 'Tidak memakai BPJS'
                    print(f"Status BPJS pasien {nama} berhasil diupdate menjadi {'Memakai BPJS' if bpjs_baru == 'Ya' else 'Tidak memakai BPJS'}.")
                    break
                else:
                    print("Input tidak valid. Silakan coba lagi.")

    print("Data pasien berhasil diperbarui.\n")

def delete_data(data_pasien):
    while True:
        print("1. Hapus data pasien tertentu\n2. Hapus semua data pasien\n3. Back to Main Menu")
        choice = input("Pilih opsi 1, 2, atau 3: ")
        if choice == '1':
            nomor_pasien = input("Masukkan nomor pasien yang ingin dihapus: ")
            nama_pasien = input("Masukkan nama pasien yang ingin dihapus: ").title()

            # Mencari pasien berdasarkan nomor dan nama
            for search in data_pasien:
                if search["Nomor_Pasien"] == nomor_pasien and search["Nama"] == nama_pasien:
                    backup = search.copy()
                    pasien_pulang.append(backup)  # Simpan data yang dihapus
                    data_pasien.remove(search)  # Hapus data dari list
                    print("Data berikut berhasil dihapus:")
                    print(tb([pasien_pulang], headers='keys', tablefmt='github'))
                    return
            else:
                print("Data tidak ditemukan, silakan inputkan kembali.")
        elif choice == '2':
            backup = data_pasien.copy() # Simpan semua data pasien ke backup
            confirm = input("Anda yakin ingin menghapus semua data pasien? (Ya/Tidak): ").capitalize()
            if confirm == 'Ya':
                data_pasien.clear() # Menghapus semua data pasien
                pasien_pulang.extend(backup) # Tambahkan semua data yang dihapus ke pasien_pulang
                print("Semua data pasien berhasil dihapus.")
                return
            else:
                print("Penghapusan semua data dibatalkan.")
        elif choice == '3':
            return  # Back to main menu
        else: 
            print("Pilihan tidak valid, silakan coba lagi.")

# Fungsi untuk menampilkan riwayat penghapusan data
def history_pasien_pulang(data_pasien):
    if pasien_pulang:
        print("Riwayat Pasien Pulang:")
        for record in pasien_pulang:
            print(tb([record], headers='keys', tablefmt='github'))
    else:
        print("Tidak ada riwayat pasien pulang.")

# Fungsi untuk mengubah status pembayaran
def pelunasan_pasien():
    pasien_belum_lunas = [pasien for pasien in data_pasien if pasien['Pembayaran'] == 'Belum'] # Fungsi untuk menampilkan status pembayaran yang belum lunas
    
    if not pasien_belum_lunas:
        print("Tidak ada pasien yang belum lunas.")
        return
    
    print("Pasien yang belum lunas:")
    print(tb(pasien_belum_lunas, headers='keys', tablefmt='github'))
    
    while True:
        nomor_pasien = input("Masukkan Nomor Pasien yang ingin dilunasi: ")
        nama_pasien = input("Masukkan nama pasien yang ingin dihapus: ").title()
        
        pasien_found = next((pasien for pasien in pasien_belum_lunas if pasien['Nomor_Pasien'] == nomor_pasien), None)
        if pasien_found:
            pasien_found['Pembayaran'] = 'Lunas' # Untuk mengubah status pembayaran menjadi lunas
            print(f"Status pembayaran pasien {pasien_found['Nama']} berhasil diupdate menjadi 'Lunas'.")
            return
        else:
            print("Nomor pasien tidak ditemukan. Silakan coba lagi.")

def main_menu():
    while True:
        print('Selamat Datang di Rumah Sakit Sehat Selamanya. Ini merupakan data pasien Rumah Sakit Sehat Selamanya')
        print('1. Show List')
        print('2. Add Pasien')
        print('3. Update Data Pasien')
        print('4. Delete Data Pasien')
        print('5. History Pasien Pulang')
        print('6. Pelunasan Pasien') 
        print('7. Exit Program')
        
        choice = input('Masukkan pilihan yang akan dipilih: ')
        if choice == '1':
            menu_1()
        elif choice == '2':
            add_pasien()
        elif choice == '3':
            update_pasien()
        elif choice == '4':
            delete_data()
        elif choice == '5':
            history_pasien_pulang()
        elif choice == '6': 
            pelunasan_pasien()
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()
