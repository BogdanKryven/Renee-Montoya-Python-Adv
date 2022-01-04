from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calc/<a>/<b>/div', methods=["GET"])
def div(a, b):
    result = int(a) / int(b)
    return render_template('div.html', div_text=f'{a} / {b} = {result}')


@app.route('/calc/<a>/<b>/sum', methods=["GET"])
def sum(a, b):
    result = int(a) + int(b)
    return render_template('sum.html', sum_text=f'{a} + {b} = {result}')


@app.route('/calc/<a>/<b>/dif', methods=["GET"])
def dif(a, b):
    result = int(a) - int(b)
    return render_template('dif.html', dif_text=f'{a} - {b} = {result}')


@app.route('/calc/<a>/<b>/mult', methods=["GET"])
def mult(a, b):
    result = int(a) * int(b)
    return render_template('mult.html', mult_text=f'{a} * {b} = {result}')


app.run(host='0.0.0.0', port=8080, debug=True)
