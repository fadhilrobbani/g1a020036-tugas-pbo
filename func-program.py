from functools import reduce

# List Daftar transaksi
transactions = [
    {"id": 1, "product": "Buku", "price": 50000},
    {"id": 2, "product": "Pensil", "price": 2000},
    {"id": 3, "product": "Pulpen", "price": 5000},
    {"id": 4, "product": "Tas", "price": 150000},
    {"id": 5, "product": "Baju", "price": 100000},
]
# Ingat bahwa di Functional programming kita perlu menerapkan pure function yang artinya kita tidak menyebabkan efek samping ke yang lain seperti mengubah data transactions secara langsung
# Maka dari itu kita gunakan build in function reduce agar mengembalikan nilai yang baru dan tidak mengubah data transactions
# Fungsi untuk mencari total harga transaksi


def total(transactions):
    return reduce(lambda acc, x: acc + x["price"], transactions, 0)

# Fungsi untuk mencari rata-rata harga transaksi


def average(transactions):
    return reduce(lambda acc, x: acc + x["price"], transactions, 0) / len(transactions)

# Fungsi untuk mencari transaksi dengan harga tertinggi


def highest(transactions):
    return reduce(lambda acc, x: x if x["price"] > acc["price"] else acc, transactions)

# Fungsi untuk mencari transaksi dengan harga terendah


def lowest(transactions):
    return reduce(lambda acc, x: x if x["price"] < acc["price"] else acc, transactions)

# Fungsi untuk mencetak daftar transaksi


def print_transactions(transactions):
    print("ID\tProduk\t\tHarga")
    for t in transactions:
        print(f"{t['id']}\t{t['product']}\t{t['price']}")


# Cetak daftar transaksi
print("Daftar Transaksi:")
print_transactions(transactions)

# Cetak total harga transaksi
print(f"Total Harga: {total(transactions)}")

# Cetak rata-rata harga transaksi
print(f"Rata-rata Harga: {average(transactions)}")

# Cetak transaksi dengan harga tertinggi
highest_transaction = highest(transactions)
print(
    f"Transaksi dengan harga tertinggi: {highest_transaction['product']} ({highest_transaction['price']})")

# Cetak transaksi dengan harga terendah
lowest_transaction = lowest(transactions)
print(
    f"Transaksi dengan harga terendah: {lowest_transaction['product']} ({lowest_transaction['price']})")
