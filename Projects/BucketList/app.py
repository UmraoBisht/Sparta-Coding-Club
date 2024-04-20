from flask import Flask, render_template, request, jsonify  # type: ignore
from connect import db

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/task", methods=["POST"])
def add_task():
    task = request.form.get("task")
    count = db.todolist.count_documents({})
    num = count + 1
    doc = {"num": num, "task": task, "isDone": False}
    db.todolist.insert_one(doc)
    return jsonify({"msg": "Task Saved!"})


@app.route("/task/done", methods=["POST"])
def task_done():
    doneTaskCount=request.form.get("doneTaskCount")
    doneTask=db.todolist.update_one({"num": int(doneTaskCount)},{"$set": {"isDone": True}})
    return jsonify({"msg": "Task Done!"})
    
@app.route("/task/undo", methods=["POST"])
def task_undo():
    undoTaskCount=request.form.get("undoTaskCount")
    doneTask=db.todolist.update_one({"num": int(undoTaskCount)},{"$set": {"isDone": False}})
    return jsonify({"msg": "Task Undo!"})

@app.route("/task/delete", methods=["POST"])
def task_delete():
    deleteTaskCount=request.form.get("deleteTaskCount")
    db.todolist.delete_one({"num": int(deleteTaskCount)})
    return jsonify({"msg": "Task Undo!"})


@app.route("/task", methods=["GET"])
def get_tasks():
    tasks = list(db.todolist.find({}, {"_id": False}))
    return jsonify(tasks)


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
