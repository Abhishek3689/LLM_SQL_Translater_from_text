from mysql import connector 

def connect_to_database():
    try:
        conn = connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="sample"
        )
        cur = conn.cursor()
        cur.execute("SELECT DATABASE();")
        print("✅ Connected to:", cur.fetchone()[0])
    except Exception as e:
        print("❌ Error:", e)
    finally:
        if 'cur' in locals(): cur.close()
        if 'conn' in locals() and conn.is_connected(): conn.close()