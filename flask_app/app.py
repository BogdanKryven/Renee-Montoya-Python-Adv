from flask import Flask, render_template, request, redirect

app = Flask(__name__)

text_global = []


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')


@app.route('/display-text/<txt>')
def text(txt):
    txt = txt.split()
    return render_template('text.html', text111=txt[0])


@app.route('/display-saved-text', methods=['GET'])
def save_text():
    global text_global
    return render_template('saved_text.html', text=text_global)


@app.route('/text/new', methods=['GET'])
def text_new():
    return render_template('text_form.html')


@app.route('/save', methods=["POST"])
def save():
    global text_global
    form = request.form
    text_global = form['text_blablabla']
    return redirect('/display-saved-text')


app.run(host='0.0.0.0', port=8080, debug=True)
