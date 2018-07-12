from flask import Flask

app = Flask(__name__)

@app.route("/<int:birthday>", methods=["GET"])
def index(birthday):
    return birthday+1

if __name__ == '__name__':
    app.run(port=5003)
