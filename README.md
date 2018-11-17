#Overview

`app` folder contains `app_original.py`
move `app_original.py` back to root where Flask is installed and rename to `app.py` to use

`hello.py` and `indeed_request.py` are the backend flask endpoint and parsing functions module respectively for the "App-in-a-day" Bottega Project on 11/16/2018

`SET FLASK_APP=""` command may be required to set local environment variable (See [LINK](http://flask.pocoo.org/docs/1.0/cli/))

Postman is preferred for testing the endpoint GET `http://localhost:5000/jobs?search=junior`, where junior is substituted with the url encoded query
Also Python requests library example
`import requests

url = "http://localhost:5000/jobs"

querystring = {"search":"runner"}

headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "cfc52c00-fc14-4375-9b73-8f54a574a7ac"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)`
