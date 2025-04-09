from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def home():
    return f"Hello World, bro!"


@app.route('/hello')
def hello():
    return "Hello world again bro!"






if __name__ == "__main__":
    app.run(debug=True)
