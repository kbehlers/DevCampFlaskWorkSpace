from flask import Flask, jsonify, request
import requests
import indeed_request
app = Flask(__name__)

@app.route('/jobs', methods=["GET"])
def hello():
    #Example: localhost:5000/jobs?search=junior
    #Retrieve url encoded arg 'search' from request
    query = request.args.get('search', '')

    #Store result of call to retrive_indeed function. Imported from indeed_request.py
    response_list = indeed_request.retrieve_indeed(query)

    #Use Flask's jsonify to prepare a response
    jsonified_string = jsonify(response_list)
    #Return JSON formatted jobs list of objects
    return jsonified_string

if __name__ == "__main__":
    app.run(debug=True)