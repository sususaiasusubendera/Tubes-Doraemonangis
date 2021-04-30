def help(role):
    if (role == "Admin"):
        print("=========================== HELP ===========================")
        print("register         : Untuk registrasi user baru.")
        print("login            : Untuk masuk ke dalam aplikasi.")
        print("carirarity       : Untuk mencari gadget berdasarkan rarity.")
        print("caritahun        : Untuk mencari gadget berdasarkan tahun ditemukan.")
        print("tambahitem       : Untuk menambahkan item ke dalam inventori.")
        print("hapusitem        : Untuk menghapus gadget dan comsumable.")
        print("ubahjumlah       : Untuk mengubah jumlah gadget dan consumable.")
        print("riwayatpinjam    : Untuk melihat riwayat peminjaman gadget.")
        print("riwayatkembali   : Untuk melihat riwayat pengembalian gadget.")
        print("riwayatambil     : Untuk melihat riwayat pengambilan consumable.")
        print("save             : Untuk menyimpan perubahan data.")
        print("help             : Untuk memberikan panduan penggunaan sistem.")
        print("exit             : Untuk keluar dari aplikasi.")
    elif (role == "User"):
        print("======================== HELP ========================")
        print("login        : Untuk masuk ke dalam aplikasi.")
        print("carirarity   : Untuk mencari gadget berdasarkan rarity.")
        print("caritahun    : Untuk mencari gadget berdasarkan tahun ditemukan.")
        print("pinjam       : Untuk melakukan peminjaman gadget.")
        print("kembalikan   : Untuk melakukan pengembalian gadget.")
        print("minta        : Untuk meminta consumable yang tersedia.")
        print("save         : Untuk menyimpan perubahan data.")
        print("help         : Untuk memberikan panduan penggunaan sistem.")
        print("exit         : Untuk keluar dari aplikasi.")    
    else: # role == "" 
        print("===================== HELP =====================")
        print("login            : Untuk masuk ke dalam aplikasi.")
        print("exit             : Untuk keluar dari aplikasi.")