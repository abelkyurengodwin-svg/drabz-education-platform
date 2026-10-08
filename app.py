from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import json
import os
from bot import get_bot_reply

app = Flask(__name__)

app.secret_key = "drabz-secret-key"

USERS_FILE = "users.json"


def load_users():
    if not os.path.exists(USERS_FILE):
        return []

    with open(USERS_FILE, "r") as file:
        return json.load(file)


def save_users(users):
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        if not name or not email or not password:
            return "Please fill in all fields. <a href='/register'>Go back</a>"

        users = load_users()

        for user in users:
            if user["email"].lower() == email.lower():
                return "Email already registered. <a href='/login'>Login here</a>" 
        new_user = {
            "name": name,
            "email": email,
            "password": generate_password_hash(password),
            "completed_lessons": []
        }

        users.append(new_user)
        save_users(users)

        return redirect(url_for("login"))


    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        users = load_users()

        for user in users:
            if user["email"].lower() == email.lower():
                if check_password_hash(user["password"], password):
                    session["user"] = user["email"]
                    session["name"] = user["name"]
                    return redirect(url_for("dashboard"))

        return "Invalid email or password. <a href='/login'>Try again</a>"

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    users = load_users()
    current_user = None

    for user in users:
        if user["email"].lower() == session["user"].lower():
            current_user = user
            break

    completed_lessons = current_user.get("completed_lessons", []) if current_user else []

    total_lessons = 5
    completed_count = len(completed_lessons)
    progress = int((completed_count / total_lessons) * 100)

    return render_template(
        "dashboard.html",
        completed_lessons=completed_lessons,
        progress=progress,
        completed_count=completed_count,
        total_lessons=total_lessons
    )

@app.route("/lessons")
def lessons():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("lessons.html")



@app.route("/lesson/3")
def lesson3():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("lesson3.html")
@app.route("/complete-lesson/3", methods=["POST"])
def complete_lesson_3():
    if "user" not in session:
        return redirect(url_for("login"))

    users = load_users()

    for user in users:
        if user["email"].lower() == session["user"].lower():
            if "completed_lessons" not in user:
                user["completed_lessons"] = []

            if 3 not in user["completed_lessons"]:
                user["completed_lessons"].append(3)

            break

    save_users(users)

    return redirect(url_for("dashboard"))


@app.route("/lesson/4")
def lesson4():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("lesson4.html")
@app.route("/lesson/5")
def lesson5():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("lesson5.html")


@app.route("/complete-lesson/4", methods=["POST"])
def complete_lesson_4():
    if "user" not in session:
        return redirect(url_for("login"))

    users = load_users()

    for user in users:
        if user["email"].lower() == session["user"].lower():
            if "completed_lessons" not in user:
                user["completed_lessons"] = []

            if 4 not in user["completed_lessons"]:
                user["completed_lessons"].append(4)

            break

    save_users(users)

    return redirect(url_for("dashboard"))

@app.route("/complete-lesson/5", methods=["POST"])
def complete_lesson_5():
    if "user" not in session:
        return redirect(url_for("login"))

    users = load_users()

    for user in users:
        if user["email"].lower() == session["user"].lower():
            if "completed_lessons" not in user:
                user["completed_lessons"] = []

            if 5 not in user["completed_lessons"]:
                user["completed_lessons"].append(5)

            break

    save_users(users)

    return redirect(url_for("dashboard"))


@app.route("/lesson/1")
def lesson1():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("lesson1.html")

@app.route("/complete-lesson/1", methods=["POST"])
def complete_lesson_1():
    if "user" not in session:
        return redirect(url_for("login"))

    users = load_users()

    for user in users:
        if user["email"].lower() == session["user"].lower():
            if "completed_lessons" not in user:
                user["completed_lessons"] = []

            if 1 not in user["completed_lessons"]:
                user["completed_lessons"].append(1)

            break

    save_users(users)

    return redirect(url_for("dashboard"))
@app.route("/lesson/2")
def lesson2():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("lesson2.html")
@app.route("/complete-lesson/2", methods=["POST"])
def complete_lesson_2():
    if "user" not in session:
        return redirect(url_for("login"))

    users = load_users()

    for user in users:
        if user["email"].lower() == session["user"].lower():
            if "completed_lessons" not in user:
                user["completed_lessons"] = []

            if 2 not in user["completed_lessons"]:
                user["completed_lessons"].append(2)

            break

    save_users(users)

    return redirect(url_for("dashboard"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))



@app.route("/chatbot", methods=["POST"])
def chatbot():
    message = request.form.get("message", "")
    reply = get_bot_reply(message)
    return {"reply": reply}
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


