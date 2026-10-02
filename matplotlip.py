import  matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,15,8,20]

plt.plot(x,y)
plt.show()

## Import data
import pandas as pd

df = pd.read_csv("matlop.csv",sep=';')
print(df.head())

print(df.columns)

df["Total"] = df["jumlah"] *df["harga_satuan"]
print(df.head())

plt.plot(df["Total"])
plt.title("Total Penjualan")
plt.xlabel("Jumlah")
plt.ylabel("Rupiah")
plt.show()

cabang = df.groupby("produk")["Total"].sum()

plt.bar(cabang.index, cabang.values)
plt.title("Penjualan per Cabang")
plt.show()

produk = df.groupby("produk")["jumlah"].sum()

plt.pie(produk.values, labels=produk.index, autopct='%1.1f%%')
plt.title("Komposisi Produk")     
plt.show()

plt.scatter(df["jumlah"], df["harga_satuan"])
plt.xlabel("jumlah")
plt.ylabel("harga")
plt.title("jumlah vs harga")
plt.show()

plt.figure(figsize=(10,5 ))

plt.plot(df["Total"], marker='o', linestyle='--')

plt.title("Grafik Penjualan")
plt.xlabel("Transaksi")
plt.ylabel("Rupiah")
plt.grid(True)

plt.show()

plt.plot(df["tanggal"], df["Total"])
plt.xticks(rotation=45)
plt.show()
