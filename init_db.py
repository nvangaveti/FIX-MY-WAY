# import sqlite3
#
# conn = sqlite3.connect('postgres.db')  # or use your existing DB path
# cursor = conn.cursor()
#
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS pothole_reports (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     email TEXT NOT NULL,
#     location TEXT NOT NULL,
#     image_path TEXT NOT NULL,
#     status TEXT DEFAULT 'Pending'
# )
# ''')
#
# conn.commit()
# conn.close()
#
# print("✅ pothole_reports table created successfully.")
