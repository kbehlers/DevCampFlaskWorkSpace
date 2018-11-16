from flask import Flask, jsonify
import requests
import indeed_request
app = Flask(__name__)

@app.route('/guide', methods=["GET"])
def hello():
    response_dict = { "hello": "world"}
    jsonified_string = jsonify(response_dict)
    return jsonified_string

if __name__ == "__main__":
    app.run(debug=True)