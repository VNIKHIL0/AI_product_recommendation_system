import sqlite3
import pandas as pd

# ✅ Connect to SQLite Database
db_path = "D:/recommendation_system/database/recommendation_system.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# ✅ Drop and recreate tables
cursor.execute("DROP TABLE IF EXISTS customers;")
cursor.execute("DROP TABLE IF EXISTS products;")

cursor.execute("""
CREATE TABLE customers (
    Customer_ID TEXT PRIMARY KEY,
    Age INTEGER,
    Gender TEXT,
    Location TEXT,
    Browsing_History TEXT,
    Purchase_History TEXT,
    Customer_Segment TEXT,
    Avg_Order_Value REAL,
    Holiday TEXT,
    Season TEXT
);
""")

cursor.execute("""
CREATE TABLE products (
    Product_ID TEXT PRIMARY KEY,
    Category TEXT,
    Subcategory TEXT,
    Price REAL,
    Brand TEXT,
    Average_Rating_of_Similar_Products REAL,
    Product_Rating REAL,
    Customer_Review_Sentiment_Score REAL,
    Holiday TEXT,
    Season TEXT,
    Geographical_Location TEXT,
    Similar_Product_List TEXT,
    Probability_of_Recommendation REAL
);
""")

# ✅ Load and Insert Customer Data
customer_file = "D:/recommendation_system/data/customer_data_collection.csv"
customer_df = pd.read_csv(customer_file)

# ✅ Drop extra column if exists
customer_df = customer_df.drop(columns=[customer_df.columns[-1]], errors="ignore")

customers_inserted = 0
for _, row in customer_df.iterrows():
    try:
        cursor.execute("""
        INSERT INTO customers 
        (Customer_ID, Age, Gender, Location, Browsing_History, Purchase_History, Customer_Segment, Avg_Order_Value, Holiday, Season)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, tuple(row))
        customers_inserted += 1
    except Exception as e:
        print(f"❌ Error inserting customer: {row['Customer_ID']} | {str(e)}")

print(f"✅ {customers_inserted} Customers Inserted Successfully!")

# ✅ Load and Insert Product Data
product_file = "D:/recommendation_system/data/product_recommendation_data.csv"
product_df = pd.read_csv(product_file)

# ✅ Debug: Print the number of columns
print(f"✅ Products DataFrame Shape: {product_df.shape}")  
print(f"✅ Products Columns: {list(product_df.columns)}")  

# ✅ Drop extra column if exists
if product_df.shape[1] > 13:
    product_df = product_df.iloc[:, :13]  # Keep only first 13 columns

products_inserted = 0
for _, row in product_df.iterrows():
    try:
        cursor.execute("""
        INSERT INTO products 
        (Product_ID, Category, Subcategory, Price, Brand, Average_Rating_of_Similar_Products, 
         Product_Rating, Customer_Review_Sentiment_Score, Holiday, Season, Geographical_Location, 
         Similar_Product_List, Probability_of_Recommendation)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, tuple(row))
        products_inserted += 1
    except Exception as e:
        print(f"❌ Error inserting product: {row['Product_ID']} | {str(e)}")

print(f"✅ {products_inserted} Products Inserted Successfully!")

# ✅ Commit and Close Connection
conn.commit()
conn.close()
print("🎉 Data insertion completed successfully!")
