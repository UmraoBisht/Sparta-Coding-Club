from flask import Flask,render_template,request,jsonify


app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/about')
def about():
    return "This is about Page"


@app.route('/info', methods=['GET'])
def info():
    receive_title=request.args.get('receive_title')
    print(receive_title)
    return jsonify({
        "result": "success",
        "msg":"GET Request"
    })


@app.route('/info', methods=['POST'])
def info_post():
    receive_title=request.form['receive_title']
    print(receive_title)
    return jsonify({
        "result": "success",
        "msg":"POST Request"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)