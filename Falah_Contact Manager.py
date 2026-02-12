## CAPSTONE PROJECT MODUL 1 ##
## MUHAMAD FAHRIZAL SAFALAH ##
## PURWADHIKA / JCDSOHAM - 006 ##
## MANAJEMEN KONTAK ##

# --- MAIN MENU ---
def main_menu():
    while True:
        print("\n=== ☎︎ KONTAK MANAGER ☎︎ ===")
        print("1. Lihat Kontak")
        print("2. Tambah Kontak")
        print("3. Edit Kontak")
        print("4. Hapus Kontak")
        print("5. Cari Kontak")
        print("6. Keluar")
        
        pilihan = input("Pilih Menu (1-6): ")
        
        if pilihan == '1': read_menu()
        elif pilihan == '2': create_menu()
        elif pilihan == '3': update_menu()
        elif pilihan == '4': delete_menu()
        elif pilihan == '5': search_menu()
        elif pilihan == '6': 
            print("Terima Kasih!")
            break
        else:
            print("Pilihan tidak ada.")

# --- DATA INITIALIZE ---
data_kontak = [
    {"nama": "Akhmad Arifin", "telepon": "081234567890", "email": "akhmaarfn@gmail.co.id", "kategori": "Keluarga"},
    {"nama": "Bono Santosa", "telepon": "081987654321", "email": "bono.s@work.com", "kategori": "Kerja"},
    {"nama": "Cristiano Ronaldo", "telepon": "085678912345", "email": "cris@goat.com", "kategori": "Teman"},
    {"nama": "Fabio Quartararo", "telepon": "081223344556", "email": "f,quart@yamaha.com", "kategori": "Lainnya"},
    {"nama": "Hayabusa", "telepon": "081122334455", "email": "hayabusa@mlbb.cn", "kategori": "Kerja"},
    {"nama": "LeBron James", "telepon": "089988776655", "email": "coolbron@nba.co.id", "kategori": "Teman"},
    {"nama": "Michael Jackson", "telepon": "081345678901", "email": "michael.jacksy@music.com", "kategori": "Keluarga"},
    {"nama": "Naruto Uzumaki", "telepon": "081299887766", "email": "naruto@anime.jpn", "kategori": "Kerja"},
    {"nama": "Sabrina Y", "telepon": "087766554433", "email": "binacantik@kiwkiw.com", "kategori": "Lainnya"},
    {"nama": "Zuck", "telepon": "085544332211", "email": "Zuck@meta.com", "kategori": "Teman"}
]

# --- FORMAT TABEL ---
def tampilkan_tabel(data_list):
    print("\n" + "-"*95)
    print(f"{'NO':<4} {'NAMA':<25} {'TELEPON':<15} {'KATEGORI':<10} {'EMAIL'}")
    print("-" * 95)

    if not data_list:
        print("   TIDAK ADA DATA YANG COCOK.")
    else:
        for index, kontak in enumerate(data_list, start=1):
            print(f"{index:<4} {kontak['nama']:<25} {kontak['telepon']:<15} {kontak['kategori']:<10} {kontak['email']}")
    print("-" * 95)

# --- FUNGSI LIHAT KONTAK (READ) ---
def read_menu():
    while True:
        print("\n--- MENU LIHAT KONTAK ---")
        print("1. Lihat Berdasarkan Kategori")
        print("2. Lihat Semua Kontak")
        print("3. Kembali ke Menu Utama")
        
        pilihan = input("Pilih (1-3): ")
        # Berdasarkan Kategori
        if pilihan == '1':
            # Sub-menu Kategori
            print("\n   Pilih Kategori:")
            print("   [1] Keluarga")
            print("   [2] Teman")
            print("   [3] Kerja")
            print("   [4] Lainnya")
            
            kat_input = input("   Masukkan Pilihan (1-4): ")
            target_kategori = ""
            
            if kat_input == '1': target_kategori = "Keluarga"
            elif kat_input == '2': target_kategori = "Teman"
            elif kat_input == '3': target_kategori = "Kerja"
            elif kat_input == '4': target_kategori = "Lainnya"
            else:
                print("   Pilihan kategori tidak valid.")
                continue
            
            hasil_filter = [k for k in data_kontak if k['kategori'] == target_kategori]
            
            print(f"\n   Menampilkan Kategori: {target_kategori}")
            tampilkan_tabel(hasil_filter)
            input("   Tekan Enter untuk lanjut...")
        # Semua Kontak
        elif pilihan == '2':
            print("\n   Menampilkan SEMUA DATA:")
            tampilkan_tabel(data_kontak)
            input("   Tekan Enter untuk lanjut...")

        elif pilihan == '3':
            break
        else:
            print("  Pilihan tidak valid.")

# --- VALIDASI EMAIL ---
def validasi_email(email):
    email = email.strip()
    
    if email.count('@') != 1: return False, "Email harus memiliki tepat satu '@'."
    if " " in email: return False, "Email tidak boleh mengandung spasi."
    if ".." in email: return False, "Email tidak boleh memiliki titik ganda (..)."

    user_part, domain_part = email.split('@')

    if not user_part: return False, "Nama user (sebelum @) kosong."
    if not user_part[0].isalnum(): return False, "User harus diawali huruf/angka."
    
    for char in user_part:
        if not (char.isalnum() or char in "._"):
            return False, f"Karakter '{char}' dilarang di user part."

    if not domain_part: return False, "Domain kosong."
    if '.' not in domain_part: return False, "Domain harus memiliki ekstensi."
    if domain_part.startswith('.') or domain_part.endswith('.'):
        return False, "Domain tidak boleh diawali/diakhiri titik."
    
    parts_domain = domain_part.split('.')
    ekstensi = parts_domain[-1]

    if not (2 <= len(ekstensi) <= 5) or not ekstensi.isalpha():
        return False, "Ekstensi domain tidak valid."

    return True, "Email Valid."

# --- VALIDASI NO TELEPON ---
def validasi_telepon(telepon):
    telepon_bersih = telepon.replace("-", "").replace(" ", "").strip()
    
    if telepon_bersih.startswith("+62"):
        telepon_bersih = "0" + telepon_bersih[3:]

    if not telepon_bersih.isdigit():
        return False, "Nomor telepon harus angka."
    
    if not (10 <= len(telepon_bersih) <= 13):
        return False, "Panjang nomor harus 10-13 digit."
    
    return True, telepon_bersih

# --- FUNGSI TAMBAH KONTAK (CREATE) ---
def create_menu():
    print("\n--- TAMBAH KONTAK BARU ---")
    
    # Loop Nama
    while True:
        nama = input("Masukkan Nama       : ").strip().title()
        if not nama:
            print("Error: Nama tidak boleh kosong.")
            continue
        
        # Cek Duplikat
        nama_sudah_ada = False
        for k in data_kontak:
            if k['nama'].lower() == nama.lower():
                nama_sudah_ada = True
                break
        if nama_sudah_ada:
            print("ERROR: Nama sudah terdaftar! Gunakan nama lain.")
        else:
            break

    # Loop Telepon
    telepon_final = ""
    while True:
        telepon = input("Masukkan Telepon    : ")
        valid, hasil = validasi_telepon(telepon)
        if valid:
            telepon_final = hasil
            # Cek Duplikat
            telepon_sudah_ada = False
            for k in data_kontak:
                if k['telepon'] == telepon_final:
                    telepon_sudah_ada = True
                    break
            if telepon_sudah_ada:
                print("ERROR: Nomor telepon sudah terdaftar!")
            else:
                break
        else:
            print(f"ERROR: {hasil}")

    # Loop Email
    email_final = ""
    while True:
        email = input("Masukkan Email      : ")
        valid, msg = validasi_email(email)
        if valid:
            email_final = email
            # Cek Duplikat
            email_sudah_ada = False
            for k in data_kontak:
                if k['email'].lower() == email_final.lower():
                    email_sudah_ada = True
                    break
            if email_sudah_ada:
                print("ERROR: Email sudah terdaftar!")
            else:
                break
        else:
            print(f"ERROR: {msg}")

    # Loop Kategori
    kategori_final = "Lainnya"
    while True:
        print("Kategori: [1] Keluarga  [2] Teman  [3] Kerja  [4] Lainnya")
        pilihan = input("Pilih (1-4): ")
        if pilihan == '1': 
            kategori_final = "Keluarga"
            break
        elif pilihan == '2': 
            kategori_final = "Teman"
            break
        elif pilihan == '3': 
            kategori_final = "Kerja"
            break
        elif pilihan == '4': 
            kategori_final = "Lainnya"
            break
        else:
            print("Pilihan salah.")

    data_kontak.append({
        "nama": nama, 
        "telepon": telepon_final, 
        "email": email_final, 
        "kategori": kategori_final
    })
    print(f"  Data '{nama}' berhasil disimpan!")
    input("   Tekan Enter untuk lanjut...")

# --- FUNGSI UBAH KONTAK (UPDATE) ---
def update_menu():
    # Menampilkan semua kontak
    tampilkan_tabel(data_kontak)
    if not data_kontak: return

    try:
        nomor = int(input("\nMasukkan NO data yang ingin diubah: "))
        idx = nomor - 1
        
        if 0 <= idx < len(data_kontak):
            kontak = data_kontak[idx]
            print(f"\nEditing: {kontak['nama']}")
            print("(Tekan ENTER jika tidak ingin mengubah data)")

            # Update Nama
            new_nama = input(f"Nama Baru [{kontak['nama']}] : ").strip()
            if new_nama:
                duplikat = False
                for i, k in enumerate(data_kontak):
                    if i != idx and k['nama'].lower() == new_nama.lower():
                        duplikat = True
                        break
                if duplikat:
                    print("ERROR: Nama sudah digunakan kontak lain.")
                else:
                    kontak['nama'] = new_nama.title()

            # Update Telepon
            while True:
                new_telp = input(f"Telepon Baru [{kontak['telepon']}] : ")
                if new_telp == "": break
                valid, hasil = validasi_telepon(new_telp)
                if valid:
                    duplikat = False
                    for i, k in enumerate(data_kontak):
                        if i != idx and k['telepon'] == hasil:
                            duplikat = True
                            break
                    if duplikat:
                        print("ERROR: Nomor telepon sudah digunakan kontak lain.")
                    else:
                        kontak['telepon'] = hasil
                        break
                else:
                    print(f"ERROR: {hasil}")

            # Update Email
            while True:
                new_mail = input(f"Email Baru [{kontak['email']}] : ")
                if new_mail == "": break
                valid, msg = validasi_email(new_mail)
                if valid:
                    duplikat = False
                    for i, k in enumerate(data_kontak):
                        if i != idx and k['email'].lower() == new_mail.lower():
                            duplikat = True
                            break
                    if duplikat:
                        print("ERROR: Email sudah digunakan kontak lain.")
                    else:
                        kontak['email'] = new_mail
                        break
                else:
                    print(f"ERROR: {msg}")
            
            # Update Kategori
            print(f"Kategori Lama: {kontak['kategori']}")
            print("[1] Keluarga  [2] Teman  [3] Kerja  [4] Lainnya")
            p = input("Kategori Baru :  ").lower()
            if p == '1': kontak['kategori'] = "Keluarga"
            elif p == '2': kontak['kategori'] = "Teman"
            elif p == '3': kontak['kategori'] = "Kerja"
            elif p == '4': kontak['kategori'] = "Lainnya"
            
            print("  Data berhasil diperbarui!")
            input("   Tekan Enter untuk lanjut...")
        else:
            print("  Nomor tidak ditemukan.")
    except ValueError:
        print("  Input harus angka.")

# --- FUNGSI HAPUS KONTAK (DELETE) ---
def delete_menu():
    tampilkan_tabel(data_kontak)
    if not data_kontak: return

    try:
        nomor = int(input("\nMasukkan No yang ingin dihapus: "))
        idx = nomor - 1
        
        if 0 <= idx < len(data_kontak):
            target = data_kontak[idx]
            print(f"\n  PERINGATAN: Menghapus data '{target['nama']}'")
            yakin = input("Yakin? (y/n): ").lower()
            if yakin == 'y':
                # Hapus dari list
                del data_kontak[idx]
                print("  Data dihapus.")
                input("   Tekan Enter untuk lanjut...")
            else:
                print("Dibatalkan.")
                input("   Tekan Enter untuk lanjut...")
        else:
            print("  Nomor tidak valid.")
    except ValueError:
        print("  Input harus angka.")

# --- FUNGSI CARI KONTAK (READ) ---
def search_menu():
    print("\n--- CARI KONTAK ---")
    keyword = input("Cari (Nama/Telp/Kategori): ").lower().strip()
    
    # Filter manual
    hasil_cari = []
    for k in data_kontak:
        if (keyword in k['nama'].lower() or 
            keyword in k['telepon'] or 
            keyword in k['kategori'].lower()):
            hasil_cari.append(k)
    
    if hasil_cari:
        print(f"\nDitemukan {len(hasil_cari)} data:")
        tampilkan_tabel(hasil_cari)
        input("   Tekan Enter untuk lanjut...")
    else:
        print("  Data tidak ditemukan.")
        input("   Tekan Enter untuk lanjut...")

# --- RUN PROGRAM ---
main_menu()