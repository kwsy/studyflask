from flask import Flask, render_template

app = Flask(__name__)


@app.route('/name/<string:name>', methods=['GET'])
def name(name):
    return render_template('name.html', name=name)


@app.route('/if/<string:name>', methods=['GET'])
def test_if(name):
    return render_template('if.html', name=name)


@app.route('/stu')
def stu():
    stu_lst = [
        {'name': '小明', 'age': 14, 'score': 98},
        {'name': '小刚', 'age': 13, 'score': 95},
        {'name': '小红', 'age': 15, 'score': 96}
    ]

    return render_template('stu.html', stu_lst=stu_lst)


if __name__ == '__main__':
    app.run(debug=True)