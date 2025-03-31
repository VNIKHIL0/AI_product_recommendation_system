import pandas as pd
from sqlalchemy import create_engine
import os

# Define file paths correctly
customer_data_path = os.path.join("..", "data", "customer_data_collection.csv")
product_data_path = os.path.join("..", "data", "product_recommendation_data.csv")

# Check if files exist before proceeding
if not os.path.exists(customer_data_path):
    raise FileNotFoundError(f"Customer data file not found: {customer_data_path}")

if not os.path.exists(product_data_path):
    raise FileNotFoundError(f"Product data file not found: {product_data_path}")

# Load CSV files
customer_df = pd.read_csv(customer_data_path)
product_df = pd.read_csv(product_data_path)

# Connect to SQLite
engine = create_engine("sqlite:///../recommendation_system.db")

# Save to database
customer_df.to_sql("customers", engine, if_exists="replace", index=False)
product_df.to_sql("products", engine, if_exists="replace", index=False)

print("Data inserted successfully!")
