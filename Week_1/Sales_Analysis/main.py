import pandas as pd

# Step 1: Read CSV
df = pd.read_csv(r"d:\Unlox\Week_1\Sales_Analysis\sales.csv")
print("📌 Original Data:")
print(df)

# Step 2: Handle Missing Values
df['Quantity'] = df['Quantity'].fillna(df['Quantity'].mean())
df['Price'] = df['Price'].fillna(df['Price'].mean())

print("\n🔧 After Handling Missing Values:")
print(df)

# Step 3: Calculate Revenue
df['Revenue'] = df['Quantity'] * df['Price']
print("\n💰 Data with Revenue Column:")
print(df)

# Step 4: Total Revenue per Product
product_revenue = df.groupby("Product")['Revenue'].sum()
print("\n📊 Total Revenue per Product:")
print(product_revenue)

# Step 5: Revenue by Date (Trend Analysis)
daily_revenue = df.groupby("Date")['Revenue'].sum()
print("\n📅 Revenue by Date:")
print(daily_revenue)
