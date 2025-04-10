import sqlite3
import ast

def recommend_products(browsing_history):
    try:
        conn = sqlite3.connect("recommendation_system.db")
        cursor = conn.cursor()

        if isinstance(browsing_history, str):
            browsing_history = ast.literal_eval(browsing_history)

        if not browsing_history:
            return []

        results = []
        for category in browsing_history:
            cursor.execute("""
                SELECT Product_ID, Category, Probability_of_Recommendation
                FROM products
                WHERE Category = ?
                ORDER BY Probability_of_Recommendation DESC
                LIMIT 2
            """, (category,))
            rows = cursor.fetchall()
            for row in rows:
                results.append({
                    "product_id": row[0],
                    "category": row[1],
                    "probability": row[2]
                })

        return results
    except Exception as e:
        print(f"🔥 Recommendation error: {e}")
        return []
