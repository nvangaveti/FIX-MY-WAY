# import psycopg2
# from config import DATABASE_CONFIG
# 
# def get_db_connection():
#     conn = psycopg2.connect(**DATABASE_CONFIG)
#     return conn
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'
# 
import psycopg2
from flask_backend.config import DATABASE_CONFIG

def insert_complaint(phone, highway, location, image_path, num_potholes, processed_path):
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO pothole_reports (phone_number, highway_name, location, image_url, pothole_count, processed_image_path)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (phone, highway, location, image_path, num_potholes, processed_path))
    conn.commit()
    cursor.close()
    conn.close()

def fetch_all_complaints():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pothole_reports ORDER BY id DESC")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
