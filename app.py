from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    department = request.form["department"]
    return f"Student Name: {name}<br>Department: {department}"

if __name__ == "__main__":
    app.run(debug=True)
