from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/<query>")
def api_query(query):
    return jsonify({"query_result":
    	[query]})

if __name__ == '__main__':
	app.run(port=5001)
