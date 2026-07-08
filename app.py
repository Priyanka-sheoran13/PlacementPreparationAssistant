from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from data.easy_questions import easy_questions
from data.medium_questions import medium_questions
from data.hard_questions import hard_questions
from python_questions import python_questions
from java_questions import java_questions
from cpp_questions import cpp_questions
from c_questions import c_questions
from sql_questions import sql_questions
from interview_questions import interview_questions
from flask import render_template, request, send_file
from company_questions import company_data
from chatbot import chatbot_responses
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///placement.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User Table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
class QuizResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    level = db.Column(db.String(20), nullable=False)

    score = db.Column(db.Integer, nullable=False)

    total = db.Column(db.Integer, nullable=False)

    percentage = db.Column(db.Integer, nullable=False)


# Quiz Question Table
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(20), nullable=False)
    question = db.Column(db.String(500), nullable=False)
    option1 = db.Column(db.String(200), nullable=False)
    option2 = db.Column(db.String(200), nullable=False)
    option3 = db.Column(db.String(200), nullable=False)
    option4 = db.Column(db.String(200), nullable=False)
    answer = db.Column(db.String(200), nullable=False)
# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email, password=password).first()

        if user:
            return redirect("/dashboard")
        else:
            return "Invalid Email or Password"

    return render_template("login.html")


# Register Page
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        new_user = User(
            name=name,
            email=email,
            password=password
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect("/login")

    return render_template("register.html")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


#create database
with app.app_context():
    db.create_all()
# ---------------- EASY QUESTIONS ----------------



@app.route("/aptitude")
def aptitude():
    return render_template("aptitude_home.html")


@app.route("/resume")
def resume():

    return render_template("resume.html")
@app.route("/interview")
def interview():

    return render_template(
        "interview.html",
        questions=interview_questions
    )
@app.route("/company")
def company():
    return render_template(
        "company.html",
        companies=company_data
    )

@app.route("/planner")
def planner():
    return render_template("planner.html")

@app.route("/progress")
def progress():
    return render_template("progress.html")
@app.route("/logout")
def logout():
    return redirect("/")
@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")
@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json.get("message", "").lower()

    reply = "🤖 Sorry! I don't understand that yet. Try asking about Python, Java, SQL, DBMS, Resume, Placement or Interview."

    for keyword, response in chatbot_responses.items():

        if keyword in user_message:

            reply = response
            break

    return jsonify({
        "reply": reply
    })
@app.route("/easy")
def easy():
    return render_template("easy_instruction.html")
@app.route("/easy-quiz")
def easy_quiz():
    return render_template(
        "easy_quiz.html",
        questions=easy_questions
    )

@app.route("/medium")
def medium():
    return render_template("medium.html", questions=medium_questions)

@app.route("/medium-result", methods=["POST"])
def medium_result():

    score = 0
    total = len(medium_questions)

    for i, q in enumerate(medium_questions):
        if request.form.get(f"q{i}") == q["answer"]:
            score += 1

    percentage = round((score / total) * 100)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    else:
        grade = "Fail"

    result = QuizResult(
        level="Medium",
        score=score,
        total=total,
        percentage=percentage
    )

    db.session.add(result)
    db.session.commit()

    return render_template(
        "medium_result.html",
        score=score,
        total=total,
        percentage=percentage,
        grade=grade
    )
@app.route("/hard")
def hard():
    return render_template(
        "hard.html",
        questions=hard_questions
    )
@app.route("/easy-result", methods=["POST"])
def easy_result():

    score = 0
    total = len(easy_questions)

    for i, q in enumerate(easy_questions):
        if request.form.get(f"q{i}") == q["answer"]:
            score += 1

    percentage = round((score / total) * 100)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    else:
        grade = "Fail"
   
   
    result = QuizResult(
        level="Easy",
        score=score,
        total=total,
        percentage=percentage
    )

    db.session.add(result)
    db.session.commit()

    return render_template(
        "easy_result.html",
        score=score,
        total=total,
        percentage=percentage,
        grade=grade
    )
@app.route("/hard-result", methods=["POST"])
def hard_result():

    score = 0
    total = len(hard_questions)

    for i, q in enumerate(hard_questions):
        if request.form.get(f"q{i}") == q["answer"]:
            score += 1

    percentage = round((score / total) * 100)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    else:
        grade = "Fail"

    return render_template(
        "hard_result.html",
        score=score,
        total=total,
        percentage=percentage,
        grade=grade
    )
@app.route("/coding")
def coding():
    return render_template("coding.html")
@app.route("/python")
def python():
    return render_template(
        "python.html",
        questions=python_questions
    )
@app.route("/c")
def c():
    return render_template(
        "c.html",
        questions=c_questions
    )

@app.route("/cpp")
def cpp():

    return render_template(
        "cpp.html",
        questions=cpp_questions
    )

@app.route("/java")
def java():

    return render_template(
        "java.html",
        questions=java_questions
    )

@app.route("/sql")
def sql():

    return render_template(
        "sql.html",
        questions=sql_questions
    )
    
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)    