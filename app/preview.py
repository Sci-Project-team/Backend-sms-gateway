import sqlite3
import pandas as pd

def view_table(table_name):
    conn = sqlite3.connect('./data/sms_gateway.db')
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df

# Example usage
print("Users:")
print(view_table('users'))

print("\nMessages:")
print(view_table('messages'))

print("\nLogs:")
print(view_table('logs'))