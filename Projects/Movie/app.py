from flask import Flask,render_template,request # type: ignore
from connect import db


app = Flask(__name__)
@app.route("/")
def home():
    return render_template('movie.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)