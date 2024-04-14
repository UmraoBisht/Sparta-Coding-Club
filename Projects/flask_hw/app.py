from flask import Flask,request,render_template,jsonify # type: ignore

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/info', methods=['GET'])
def get_info():
    my_name=request.args['my_name']
    print(my_name)
    return jsonify({
        "my_name":my_name,
        "my_age":20
    })


@app.route('/info', methods=['POST'])
def post_info():
    my_name=request.form.get('my_name')
    print(my_name)
    return jsonify({
        "my_name":my_name,
        "my_age":20
    })


if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)

