kendaraan = ["Honda Civic", "Sedan", "1600 cc", "Biru", "4"]
merk_kendaraan = "Honda"
harga_kendaraan = "Rp 250.000.000"
tipe_kendaraan = "Baru"

indeks_sedan = kendaraan.index("Sedan")

kendaraan.insert(indeks_sedan + 1, merk_kendaraan)

kendaraan.append(harga_kendaraan)
kendaraan.append(tipe_kendaraan)