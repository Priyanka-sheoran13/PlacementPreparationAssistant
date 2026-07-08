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
    return render_template("sql.html")
    
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)    