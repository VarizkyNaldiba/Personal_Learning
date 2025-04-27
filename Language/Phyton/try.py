def persegi_panjang(p, l):
    luas = p * l
    keliling = 2 * (p + l)
    print("Luas Persegi Panjang:", luas)
    print("Keliling Persegi Panjang:", keliling)

def segitiga(a, t):
    luas = 0.5 * a * t
    keliling = a + t + (a**2 + t**2)**0.5  # Menggunakan teorema Pythagoras untuk sisi miring
    print("Luas Segitiga:", luas)
    print("Keliling Segitiga:", keliling)

def main():
    print("Pilih bangun datar:")
    print("1. Persegi Panjang")
    print("2. Segitiga")
    pilihan = input("Masukkan pilihan (1/2): ")

    if pilihan == "1":
        p = int(input("Masukkan panjang: "))
        l = int(input("Masukkan lebar: "))
        persegi_panjang(p, l)
    elif pilihan == "2":
        a = int(input("Masukkan alas: "))
        t = int(input("Masukkan tinggi: "))
        segitiga(a, t)
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
