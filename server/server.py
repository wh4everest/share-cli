from flask import Flask
app = Flask(__name__)

app.debug = True

@app.route("/", methods=['POST'])
def hello():
    return "Hello World!"
