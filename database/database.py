import sqlite3

# Create and connect to SQLite database
conn = sqlite3.connect("recommendation_system.db")
cursor = conn.cursor()

# Create Customers Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    location TEXT
)
""")

# Create Products Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL
)
""")

conn.commit()
conn.close()

print("Database created successfully!")
