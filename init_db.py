import sqlite3

# ✅ Connect to DB (users.db file create ho jayegi agar pehle se nahi hai)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# ✅ Users table (for register/login)
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# ✅ Predictions table (for saving prediction history)
cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    inputs TEXT,
    result TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

# ✅ Commit and close
conn.commit()
conn.close()

print("✅ Database initialized with users and predictions tables")
