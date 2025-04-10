import sqlite3

def get_customer_data(customer_id: str):
    try:
        conn = sqlite3.connect("api/recommendation_system.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT Customer_ID, Age, Gender, Location, Browsing_History, Purchase_History, Customer_Segment, Season
            FROM customers
            WHERE Customer_ID = ?
        """, (customer_id,))

        row = cursor.fetchone()
        if row:
            return {
                "customer_id": row[0],
                "age": row[1],
                "gender": row[2],
                "location": row[3],
                "browsing_history": row[4],
                "purchase_history": row[5],  # ✅ NEW
                "segment": row[6],
                "season": row[7]
            }
        else:
            return None
    except Exception as e:
        print(f"🔥 Error: {e}")
        return None
