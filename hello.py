from flask import Flask, jsonify, request
import json
import requests
import indeed_request
app = Flask(__name__)

Data = []

@app.route('/jobs', methods=["GET","POST"])
def hello():
    if request.method == 'GET':
        # response_dict = indeed_request.parse_indeed('output.txt')
        # jsonified_string = jsonify(response_dict)
        # return jsonified_string
        query = request.args.get('query', '')
        print(query)
        response_list = indeed_request.retrieve_indeed(query)
        jsonified_string = jsonify(response_list)
        return jsonified_string
    if request.method == 'POST':
        # query = request.form.get('search')
        query=request.data.decode("utf-8", "replace")
        query = request.data
        query = json.loads(query)
        query = query['search']
        response_list = indeed_request.retrieve_indeed(query)
        # print(response_list)
        jsonified_string = jsonify(response_list)
        # jsonified_string.headers.add('Access-Control-Allow-Origin', '*')
        # jsonified_string.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        # jsonified_string.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        # jsonified_string.headers["Content-Type"] = "application/json"
        Data = response_list

        print(Data)

        return jsonified_string
        # return app.response_class(
        #     response=json.dumps(response_list),
        #     status=200,
        #     mimetype='application/json'
        # )


@app.route('/')
def return_data():
    print(Data)
    jsonified_string = jsonify(Data)
    return jsonified_string


if __name__ == "__main__":
    app.run(debug=True)