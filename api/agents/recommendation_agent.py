import sqlite3

def get_customer_preferences(customer_id: str):
    try:
        conn = sqlite3.connect("./api/recommendation_system.db")
        cursor = conn.cursor()

        print(f"🔍 Checking database for customer_id: '{customer_id}'")  # Debugging Log

        # Fetch browsing history
        cursor.execute("SELECT Browsing_History FROM customers WHERE Customer_ID = ?", (customer_id,))
        row = cursor.fetchone()

        if row and row[0]:
            browsing_history = row[0].strip()  # Remove extra spaces
            print(f"✅ Found Browsing History: {browsing_history}")  # Debugging Log
            return browsing_history
        else:
            print(f"⚠️ No Browsing History found for Customer ID {customer_id}")
            return None

    except Exception as e:
        print(f"🔥 Database error: {e}")
        return None
    finally:
        conn.close()
