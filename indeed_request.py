import requests
import pprint

def retrieve_indeed():
    r = requests.get("https://www.indeed.com/jobs?q=junior&l=Orem%2C+UT&radius=25")
    pprint.pprint(r.text)

retrieve_indeed()