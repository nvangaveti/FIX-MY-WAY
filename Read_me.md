# Fix My Way - Pothole Detection and Complaint System 🚧

**Developed by Team FIX MY WAY**

## About
Fix My Way is an AI-powered pothole detection system designed to help local authorities identify and repair potholes in highways. Using state-of-the-art machine learning techniques, the system detects potholes and provides a user-friendly interface for citizens to report problems.

This project aims to reduce road accidents and improve the infrastructure by enabling efficient pothole detection and reporting.

---

## Features
- Real-time pothole detection
- Easy complaint submission form
- Database to store pothole reports
**Fix My Way** is a full-stack web and machine learning project aimed at detecting potholes on highways (focused on Madhya Pradesh) and streamlining the complaint registration process.  
It empowers users to report potholes, automatically validates them using an AI model, and stores authentic complaints for authorities to take action.

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python Flask
- **Database:** PostgreSQL
- **Machine Learning:** YOLOv8 (trained with annotated images from Roboflow)
- **Deployment:** (to be added if deployed)

---

## 📷 Machine Learning Model

- **Model Used:** YOLOv8
- **Dataset:** Kaggle pothole dataset, annotated via Roboflow
- **Training:** Fine-tuned for pothole detection specific to Indian roads.
- **Purpose:** Automatically validates user-submitted pothole images before accepting complaints.

---

## 📚 How It Works

1. **User Interface:**  
   Users access a web form to submit pothole complaints, including images and location details.

2. **Image Validation:**  
   Submitted images are processed by a YOLOv8 model hosted on the Flask backend to confirm the presence of a pothole.

3. **Database Storage:**  
   Only validated pothole complaints are saved into the PostgreSQL database for further action.

4. **Result:**  
   Authorities can easily filter and view genuine pothole complaints.

---

## 🚀 Project Setup

### Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

# Install dependencies
pip install -r requirements.txt

# Run the Flask server
python app.py
```

### Frontend Setup
No heavy setup needed. Simply open the `test_2.html` file inside your browser, or use any basic local server (like Live Server Extension in VS Code).

### Database Setup
- Install and run PostgreSQL.
- Create a database (e.g., `fixmyway_db`).
- Update your Flask app with your DB credentials.
- Run any provided SQL migration scripts.

---

## 📁 Project Structure

```
Fix-My-Way/
|
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
|
├── backend/
│   ├── app.py
│   ├── model/
│   │   └── pothole_detection_model.pt
│   ├── database/
│   │   └── db.py
│   └── requirements.txt
|
└── README.md
```

---

## 🎯 Future Improvements

- Deploy the model and server online (AWS, Render, Heroku).
- Build an admin dashboard for monitoring.
- Add SMS/Email notification features.
- Expand model capabilities to detect other road issues (cracks, speed bumps, etc).

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements
This project was developed by **Team FIX MY WAY**:
1. Nikhil Vangaveti
2. D.Maheedhar Naidu
3. Karanam Charan Teja
4. D.Ruthik Sumesh
5. Thiruveedula Rohit
6. Vangaveti Shiva Saketh
7. T.Parvath Reddy



- >[Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- >[Roboflow](https://roboflow.com/)
- >Kaggle Datasets
- >Flask and PostgreSQL documentation
- >Some parts of this project were generated using ChatGPT.


---
