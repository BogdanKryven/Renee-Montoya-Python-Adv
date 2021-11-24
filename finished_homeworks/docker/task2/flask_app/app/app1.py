from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "Welcome_2_variable"


@app.route('/hello')
def hello():
    return 'Hi there!_2_variable'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
