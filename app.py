from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import joblib
import numpy as np
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "your_secret_key"   # session ke liye zaroori hai

# Load trained model
model = joblib.load("best_model.pkl")

# ✅ Correct feature list
feature_cols = [
 'mld_res', 'mld_ps_res', 'card_rem', 'ratio_Rrem', 'ratio_Arem',
 'jaccard_RR', 'jaccard_RA', 'jaccard_AR', 'jaccard_AA',
 'jaccard_ARrd', 'jaccard_ARrem'
]

# ---------------- AUTH ROUTES ---------------- #

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # ✅ Hash password before saving
        hashed_pw = generate_password_hash(password)

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username,password) VALUES (?,?)",(username,hashed_pw))
            conn.commit()
            return redirect(url_for("login"))
        except:
            return "❌ Username already exists"
        finally:
            conn.close()
    return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        user = cursor.execute("SELECT * FROM users WHERE username=?",(username,)).fetchone()
        conn.close()

        if user and check_password_hash(user["password"], password):
            session["user"] = username
            return redirect(url_for("home"))
        else:
            return "❌ Invalid credentials"
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

# ---------------- MAIN APP ROUTES ---------------- #

@app.route("/")
def home():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "user" not in session:
        return redirect(url_for("login"))

    try:
        values = []
        for f in feature_cols:
            val = request.form.get(f)
            if val is None or val.strip() == "":
                return render_template("index.html", prediction_text=f"❌ Missing value for {f}")
            
            num = float(val)

            # ✅ Range checks
            if f.startswith("jaccard") and not (0 <= num <= 1):
                return render_template("index.html", prediction_text=f"❌ Invalid value for {f}, must be between 0 and 1")
            if f in ["mld_res", "mld_ps_res"] and num not in [0,1]:
                return render_template("index.html", prediction_text=f"❌ Invalid value for {f}, must be 0 or 1")

            values.append(num)

        final = np.array(values).reshape(1, -1)
        prediction = model.predict(final)[0]

        if prediction == 1:
            result = "⚠️ Phishing Website"
        else:
            result = "✅ Safe Website"

        # ✅ Save to DB instead of JSON
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO predictions (username, inputs, result) VALUES (?,?,?)",
                       (session["user"], str(values), result))
        conn.commit()

        # ✅ Fetch last 5 predictions
        cursor.execute("SELECT timestamp, result FROM predictions WHERE username=? ORDER BY id DESC LIMIT 5",
                       (session["user"],))
        history = cursor.fetchall()
        conn.close()

        return render_template("index.html", prediction_text=result, history=history)

    except Exception as e:
        return render_template("index.html", prediction_text=f"❌ Error: {str(e)}")


# ✅ Flask entry point
if __name__ == "__main__":
    app.run(debug=True)
