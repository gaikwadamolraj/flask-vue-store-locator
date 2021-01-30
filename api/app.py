from flask import Flask, request, jsonify
from util import findStore

app = Flask(__name__)

@app.route("/api/helath")
def hello():
    return "hello !!!"

@app.route("/api/stores")
def findStores():
    return jsonify(findStore(request))

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=8889)
