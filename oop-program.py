# Kelas untuk entitas Transaksi
class Transaction:
    # Membuat constructor di python  untuk menginisialisasi nilai-nilai awal objek
    # Kelas Transaction mempunyai 3 atribut yaitu id, product, dan price
    def __init__(self, id, product, price):
        self.id = id
        self.product = product
        self.price = price

# Kelas sebagai entitas daftar dari Transaksi


class TransactionList:
    # Membuat constructor di python  untuk menginisialisasi nilai-nilai awal objek
    # Kelas TransactionList mempunyai 1 atribut yaitu transactions
    def __init__(self, transactions):
        self.transactions = transactions

# Fungsi untuk mencari total harga transaksi
    def total(self):
        return sum(t.price for t in self.transactions)

# Fungsi untuk mencari rata-rata harga transaksi
    def average(self):
        return self.total() / len(self.transactions)

# Fungsi untuk mencari transaksi dengan harga tertinggi
    def highest(self):
        return max(self.transactions, key=lambda t: t.price)

# Fungsi untuk mencari transaksi dengan harga terendah
    def lowest(self):
        return min(self.transactions, key=lambda t: t.price)

# Fungsi untuk mencetak daftar transaksi
    def print_transactions(self):
        print("ID\tProduk\t\tHarga")
        for t in self.transactions:
            print(f"{t.id}\t{t.product}\t{t.price}")


# List Daftar transaksi
transactions = [
    Transaction(1, "Buku", 50000),
    Transaction(2, "Pensil", 2000),
    Transaction(3, "Pulpen", 5000),
    Transaction(4, "Tas", 150000),
    Transaction(5, "Baju", 100000)
]

# Buat objek TransactionList
transaction_list = TransactionList(transactions)

# Cetak daftar transaksi
print("Daftar Transaksi:")
transaction_list.print_transactions()

# Cetak total harga transaksi
print(f"Total Harga: {transaction_list.total()}")

# Cetak rata-rata harga transaksi
print(f"Rata-rata Harga: {transaction_list.average()}")

# Cetak transaksi dengan harga tertinggi
highest_transaction = transaction_list.highest()
print(
    f"Transaksi dengan harga tertinggi: {highest_transaction.product} ({highest_transaction.price})")

# Cetak transaksi dengan harga terendah
lowest_transaction = transaction_list.lowest()
print(
    f"Transaksi dengan harga terendah: {lowest_transaction.product} ({lowest_transaction.price})")
