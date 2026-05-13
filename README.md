# ⚠️ Phishing URL Detection System

A Machine Learning based web application that detects whether a website URL is safe or phishing using Flask and Python.

---

# 🚀 About The Project

Phishing websites are fake websites designed to steal sensitive information such as passwords, banking details, and personal data.  
This project helps users identify whether a URL is legitimate or phishing using a trained Machine Learning model.

The user simply enters a website URL into the system, and the application analyzes the URL features to predict whether the website is safe or dangerous.

This project is built using:
- Python
- Flask
- Machine Learning
- HTML
- CSS
- JavaScript

---

# 📥 Input

The user provides:
- A website URL

Example:

```bash
https://example.com
```

---

# 📤 Output

The system predicts one of the following results:

- ✅ Legitimate Website
- ⚠️ Suspicious Website
- ❌ Phishing Website

The prediction result is displayed instantly on the screen.

---

# ✨ Features

- Machine Learning based phishing detection
- Fast URL prediction
- User-friendly interface
- Responsive design
- Flask backend integration
- Prediction history storage
- Real-time result display

---

# 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML
- CSS
- JavaScript

---

# 📂 Project Structure

```bash
project/
│
├── app.py
├── best_model.pkl
├── history.json
│
├── templates/
│   └── index.html
│
└── static/
    ├── css/
    ├── js/
    └── images/
```

---

# ▶️ How To Run The Project

## Step 1: Install Required Libraries

```bash
pip install -r requirements.txt
```

## Step 2: Run Flask Application

```bash
python app.py
```

## Step 3: Open Browser

```bash
http://127.0.0.1:5000
```

---

# ⚙️ Working Process

1. User enters a URL
2. The system extracts URL features
3. Features are sent to the trained ML model
4. The model predicts whether the URL is phishing or legitimate
5. Result is displayed to the user

---

# 👨‍💻 Author

Hasan Pasha

---
