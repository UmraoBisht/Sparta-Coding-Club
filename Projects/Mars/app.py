from flask import Flask, render_template, jsonify, request # type: ignore
from connect import db


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/create", methods=["POST"])
def create_land():
    print(db)
    name = request.form.get("name")
    address = request.form.get("address")
    acres = request.form.get("acre")
    doc = {'name': name, 'address': address, 'acres': acres}
    db.orders.insert_one(doc)
    return jsonify({"result": "success", "msg": "Created"})


@app.route("/land_records", methods=["GET"])
def land_records():
    order_list = list(db.orders.find({}, {'_id': False}))
    return jsonify({"order_list": order_list})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
