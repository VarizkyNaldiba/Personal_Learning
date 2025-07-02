import sys
import datetime
import pandas as pd

#1
# print("python version")
# print(sys.version+ "\n")
# print("version info")
# print(sys.version_info)

#2
# print("current date and time")
# current_date_time = datetime.datetime.now()
# print(current_date_time.strftime("%Y-%m-%d %H:%M:%S"))


#3
data = pd.read_csv("retail_sales_dataset.csv")
print(data.head()) # Display the first 5 rows of the DataFrame
print(data.info()) # Display information about the DataFrame
print(data.describe()) # Display summary statistics of the DataFrame
print(data.columns) # Display the column names of the DataFrame
print(data.shape) # Display the shape of the DataFrame (rows, columns)
data["Date"] = pd.to_datetime(data["Date"]) # Convert the "Date" column to datetime format
data['Month'] = data['Date'].dt.month_name() # Extract the month from the "Date" column

penjualan_per_bulan = data.groupby("Month")["Total Amount"].sum().sort_values(ascending=False) # Group by month and sum the "Total Amount" for each month, then sort in descending order
print(penjualan_per_bulan) # Display total sales per month sorted in descending order

#### Note: Gabisa sort 2 sekaligus, jadi harus satu-satu

penjualan_paling_laris = data.groupby("Product Category")["Quantity"].sum().sort_values(ascending=False).head(10) # Group by product and sum the "Quantity", then sort in descending order and take the top 10
print(penjualan_paling_laris) # Display the top 10 best-selling products

pendapatan_per_produk = data.groupby("Product Category")["Total Amount"].sum().sort_values(ascending=False) # Group by product and sum the "Total Amount", then sort in descending order
print(pendapatan_per_produk) # Display total revenue per product sorted in descending order