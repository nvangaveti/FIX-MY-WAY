from flask import Flask, render_template, request, redirect, url_for
import os
import uuid
import psycopg2
from flask_backend.db import insert_complaint, fetch_all_complaints
from flask import Flask, render_template
from ultralytics import YOLO
from werkzeug.utils import secure_filename
from datetime import datetime
from pothole_detect import detect_potholes


app = Flask(__name__)

# Set up upload and detection folders
UPLOAD_FOLDER = 'flask_backend/static/uploads'
DETECTED_FOLDER = 'flask_backend/detected_potholes'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'mp4', 'avi', 'mov'}



model = YOLO(r'C:\Users\vanga\OneDrive\Desktop\yolov8-roadpothole-detection-main\flask_backend\best.pt')


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DETECTED_FOLDER'] = DETECTED_FOLDER



# Helper function to check file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Home page
@app.route('/')
def index():
    return render_template('test_2.html')  # You should have this HTML form

#dashcam
@app.route('/dashcam')
def dashcam():
    return render_template('dashcam.html')

# Upload route

@app.route('/upload', methods=['GET'])
def show_upload_form():
    return render_template('upload.html')


# ✅ 2. Handle Upload Form Submission (POST request)
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    phone = request.form.get('phone')
    highway = request.form.get('highway')
    location = request.form.get('location')

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        unique_name = f"{uuid.uuid4().hex}_{filename}"
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_name)
        file.save(upload_path)

        # Your function to process image and count potholes
        processed_img_path, num_potholes = detect_potholes(upload_path)

        # Save to DB (replace with your DB insert function)
        detected_rel_path = os.path.relpath(processed_img_path, 'flask_backend/static')
        insert_complaint(phone, highway, location, f'uploads/{unique_name}', num_potholes, detected_rel_path)

        return redirect(url_for('complaint_history'))

    return 'Invalid file type'



@app.route('/devicecam', methods=['GET', 'POST'])
def devicecam():
    if request.method == 'POST':
        image = request.files['image']
        phone = request.form['phone']
        highway = request.form['highway']

        filename = secure_filename(image.filename)
        unique_name = f"{uuid.uuid4().hex}_{filename}"
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_name)
        image.save(upload_path)

        # YOLOv8 detection
        processed_img_path, pothole_count = detect_potholes(upload_path)

        # Save to DB
        location = "User captured location (optional)"
        original_rel_path = os.path.relpath(upload_path, 'flask_backend/static')
        detected_rel_path = os.path.relpath(processed_img_path, 'flask_backend/static')
        insert_complaint(phone, highway, location, original_rel_path, pothole_count, detected_rel_path)

        return redirect(url_for('complaint_history'))

    return render_template('devicecam.html')



# Complaint History page


@app.route('/complaint_history')

@app.route("/complaint_history")
def complaint_history():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Nikhil123"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM pothole_reports ORDER BY id DESC")
    complaints = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("complaint_history.html", complaints=complaints)


if __name__ == '__main__':
    app.run(debug=True, port=5050 ,use_reloader=False)

