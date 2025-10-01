# Program Kategori Produk Siti

# Input data produk
jenis = input("Masukkan jenis produk (Elektronik,Pakaian,Makanan,Kosmetik): ")
harga = int(input("Masukkan harga produk (Rp): "))
penjualan = int(input("Masukkan jumlah penjualan produk: "))

# Menentukan kategori berdasarkan jenis produk
if jenis  == "elektronik":
    kategori = "Elektronik"
elif jenis  == "pakaian":
    kategori = "Pakaian"
elif jenis == "makanan":
    kategori = "Makanan"
elif jenis == "kosmetik":
    kategori = "Kosmetik"
else:
    kategori = "Lainnya"

# Menentukan label harga
if harga > 100000:
    label_harga = "Premium"
elif 50000 <= harga <= 100000:
    label_harga = "Menengah"
else:
    label_harga = "Terjangkau"

# Menentukan status penjualan
if penjualan >= 100:
    status = "Best Seller"
elif 50 <= penjualan <= 99:
    status = "Populer"
else:
    status = "Normal"

# Output hasil
print("\n=== Hasil Kategori Produk ===")
print("Kategori Produk :", kategori)
print("Label Harga     :", label_harga)
print("Status Penjualan:", status)