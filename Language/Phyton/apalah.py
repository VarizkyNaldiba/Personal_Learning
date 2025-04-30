belanja = {
    'baju': 100000,
    'celana': 150000,
    'Handphone': 2000000,
    'Laptop': 5000000,
}
barang = ['baju', 'celana', 'Handphone', 'Laptop']
total = 0

def rataRata():
    hasilMean = sum(belanja.values()) / len(belanja)  # len untuk menghitung jumlah data(nilai n)
    print("Rata-rata belanja kebutuhan kampus adalah:")
    return hasilMean

def minMax():
    min_value = min(belanja.values())  # Renamed variable to avoid conflict with built-in min()
    max_value = max(belanja.values())  # Renamed variable to avoid conflict with built-in max()
    print("Harga terendah adalah:")
    print(min_value)
    print("Harga tertinggi adalah:")
    print(max_value)

def sorting():
    print("\nDaftar belanja kebutuhan kampus:")
    print(sorted(barang))  # Urut naik
    print("\nDaftar harga belanja kebutuhan kampus:")
    print(sorted(belanja.values(), reverse=True))  # Urut turun

# Uncommented listBelanja function for better output
def listBelanja():
    print('Daftar belanja kebutuhan kampus:')
    for barang, harga in belanja.items():
        print(f'{barang}: Rp{harga}')

# Call functions to display results
sorting()
print(f"\n{rataRata()}")
minMax()
listBelanja()