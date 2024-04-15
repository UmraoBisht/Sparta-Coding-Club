from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/info", methods=["GET"])
def get_info():
    return jsonify({"name": "John", "lastname": "Buren"})


@app.route("/info", methods=["POST"])
def post_info():
    return jsonify({"name": "John", "lastname": "Buren"})


@app.route("/info", methods=["PUT"])
def put_info():
    return jsonify({"name": "John", "lastname": "Buren"})


@app.route("/info", methods=["DELETE"])
def delete_info():
    return jsonify({"name": "John", "lastname": "Buren"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
