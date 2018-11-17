from flask import Flask, jsonify, request
import requests
import indeed_request
app = Flask(__name__)

@app.route('/jobs', methods=["GET","POST"])
def hello():
    def returned_data(data):
        return data
    Data = returned_data("Hey")
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
        
        return "Hello"
        # query = request.form.get('query')
        # response_list = indeed_request.retrieve_indeed(query)
        # jsonified_string = jsonify(response_list)
        # return jsonified_string

if __name__ == "__main__":
    app.run(debug=True)