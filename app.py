from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")

@app.route('/mycv')
def mycv():
    return render_template("cv.html")

@app.route("/records")
def records():
    return render_template("records.html")

if __name__ == "__main__":
    app.run(debug = True)