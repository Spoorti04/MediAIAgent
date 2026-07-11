from flask import Flask, render_template, request
from backend.rag import ask_health_advisor

app = Flask(__name__)


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/chat")
def chat():
    return render_template("chat.html")


@app.route("/ask", methods=["POST"])
def ask():

    question = request.form["question"]

    answer = ask_health_advisor(question)

    return render_template(
        "chat.html",
        question=question,
        answer=answer
    )


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)