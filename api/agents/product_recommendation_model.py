import sqlite3
import ast  # To convert string to list

def recommend_products(browsing_history):
    try:
        conn = sqlite3.connect("D:/recommendation_system/api/recommendation_system.db")
        cursor = conn.cursor()

        print(f"🔍 Fetching products for preferences: {browsing_history}")  # Debugging Log

        # Convert string to list if needed
        if isinstance(browsing_history, str):
            browsing_history = ast.literal_eval(browsing_history)  # Convert to list

        # If browsing history is empty, return no recommendations
        if not browsing_history:
            return ["No recommendations available"]

        # Fetch recommended products from `products` table
        recommended_products = []
        for category in browsing_history:
            cursor.execute("SELECT Product_ID FROM products WHERE Category = ? LIMIT 3", (category,))
            products = cursor.fetchall()
            recommended_products.extend([row[0] for row in products])

        # If no products found, return default message
        if not recommended_products:
            return ["No recommendations available"]

        return recommended_products

    except Exception as e:
        print(f"🔥 Error in recommendation logic: {e}")
        return ["No recommendations available"]
