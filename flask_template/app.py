from flask import Flask, render_template

app = Flask(__name__)


@app.route('/name/<string:name>', methods=['GET'])
def name(name):
    return render_template('name.html', name=name)


@app.route('/if/<string:name>', methods=['GET'])
def test_if(name):
    return render_template('if.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)