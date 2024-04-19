from flask import Flask, render_template, request, jsonify # type: ignore

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/bucket", methods=["POST"])
def bucket_post():
    sample_receive = request.form["sample_give"]
    print(sample_receive)
    return jsonify({"msg": "POST /bucket request!"})


@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    sample_receive = request.form["sample_give"]
    print(sample_receive)
    return jsonify({"msg": "POST /bucket/done request!"})


@app.route("/bucket", methods=["GET"])
def bucket_get():
    return jsonify({"msg": "GET request!"})


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
