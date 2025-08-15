# Fix My Way 🚗🛣️  
**AI-Powered Pothole Detection & Reporting System**

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-black?logo=flask)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Object%20Detection-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Overview
**Fix My Way** is an AI-driven solution to detect and report potholes using computer vision.  
It uses **YOLOv8** for pothole detection from dashcam video streams or uploaded images, automatically logs the pothole details with GPS location, and stores them in a **PostgreSQL** database.  

The system offers:
- **Automatic Detection Mode** (Dashcam)  
- **Manual Complaint Registration**  
- **Complaint History Viewer**  

---

## 🚀 Features
✅ **Real-Time Detection** – From live dashcam or uploaded videos/images.  
✅ **Automatic Location Capture** – GPS coordinates auto-filled in reports.  
✅ **Manual Reporting Option** – Upload images for manual pothole complaint registration.  
✅ **Complaint History** – Combined log of automatic & manual reports.  
✅ **Processed Image Storage** – Bounding box visualizations stored for each detection.  
✅ **PostgreSQL Storage** – Organized storage in `pothole_reports` table.

---

## 🛠️ Tech Stack
| Component       | Technology Used |
|----------------|----------------|
| **Frontend**   | HTML, CSS, JavaScript |
| **Backend**    | Python (Flask) |
| **Database**   | PostgreSQL |
| **AI Model**   | YOLOv8 (Ultralytics) |
| **Libraries**  | psycopg2, OpenCV, geolocation APIs |

---

## 📂 Database Schema
**Table:** `pothole_reports`  
| Field Name           | Type         | Description |
|----------------------|--------------|-------------|
| id                   | SERIAL       | Primary Key |
| phone_number         | VARCHAR(15)  | Reporter contact |
| highway_name         | VARCHAR(255) | Highway or road name |
| location             | VARCHAR(255) | GPS coordinates |
| image_url            | TEXT         | Original uploaded image URL |
| detected_count       | INT          | Number of potholes detected |
| processed_image_url  | TEXT         | Image with bounding boxes |

---

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/fix-my-way.git
cd fix-my-way
```

### 2️⃣ Setup Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Requirements
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Database
Edit `config.py` with your PostgreSQL credentials.  
Run:
```sql
CREATE TABLE pothole_reports (
    id SERIAL PRIMARY KEY,
    phone_number VARCHAR(15),
    highway_name VARCHAR(255),
    location VARCHAR(255),
    image_url TEXT,
    detected_count INT,
    processed_image_url TEXT
);
```

### 5️⃣ Run Flask App
```bash
python app2.py
```

---

## 📜 License
This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Contributors
This project was developed by **Team FIX MY WAY**:
1. Nikhil Vangaveti
2. D.Maheedhar Naidu
3. Karanam Charan Teja
4. D.Ruthik Sumesh
5. Thiruveedula Rohit
6. Vangaveti Shiva Saketh
7. T.Parvath Reddy

---

## 🙌 Acknowledgements
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [Flask](https://flask.palletsprojects.com/)
- [PostgreSQL](https://www.postgresql.org/)
