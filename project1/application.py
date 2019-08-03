import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    # return "Project 1: TODO"
    user_id = session.get("user_id", None)
    if user_id:
        username = db.execute(
            "SELECT username FROM users WHERE id = :id", {"id": user_id}
        ).fetchone()
        username = username[0]
    else:
        username = None

    return render_template("index.html", username=username)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if (
            db.execute(
                "SELECT * FROM users WHERE username = :username",
                {"username": username},
            ).rowcount
            != 0
        ):
            return render_template(
                "error.html",
                event="Registration",
                message="ERROR User already exists",
            )
        db.execute(
            "INSERT INTO users (username, password) "
            "VALUES (:username, :password)",
            {"username": username, "password": password},
        )
        db.commit()
        return render_template("success.html", event="Registration")
    return render_template("register.html")


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = db.execute(
            "SELECT id FROM users WHERE "
            "username = :username and password = :password",
            {"username": username, "password": password},
        ).fetchone()
        if user is None:
            return render_template(
                "error.html",
                event="Sign in",
                message="ERROR invalid username or password",
            )
        session["user_id"] = user[0]

        return render_template("success.html", event="Sign In")
    return render_template("signin.html")


@app.route("/logout")
def logout():
    del session["user_id"]
    return render_template("success.html", event="Log out")
