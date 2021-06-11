pilihan = "y"
while pilihan == "y":
    print(""""
    ===========================
    
    Fitrah Coffee
    List Menu Minuman Kopi
    
    ==========================
    A. Coffee Latte : Rp 38.000
    B. Americano : Rp 42.000
    C. Espresso : Rp. 35.000
    ===========================
    """)
    pesan = str(input("masukkan list abjad menu kopi ="))
    jumlahpesan = int(input("masukkan jumlah pesanan ="))
    if pesan == "a":
        listnama = "Coffee Latte"
        harga = (38000 * jumlahpesan)

    elif pesan == "b":
        listnama = "Americano"
        harga = (42000 * jumlahpesan)

    elif pesan == "c":
        listnama = "Americano"
        harga = (35000 * jumlahpesan)

    else:
        listnama = "-"
        harga ="-"
        totalharga ="-"
        pilihan = input("menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali Y/N =")

    print("-------------------------")
    print("Fitrah Coffee")
    print("-------------------------")
    print("Menu :", listnama)
    print("Jumlah pesan :", jumlahpesan)
    print("Harga :", harga)
    print("-------------------------")
    print("Jumlah Bayar :", harga)
    print("-------------------------")
    pilihan = input("apakah anda ingin order kembali Y/N =")
