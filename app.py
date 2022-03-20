from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Lmao this is my X-tra-Userbot Server now GTFO!!</h1>"

@app.route("/xtrabot/")
def test():
    os.system("python -m xtrabot")
    return "this wont work"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
