import requests
import pprint
import json
from bs4 import BeautifulSoup

# def retrieve_indeed():
#     r = requests.get("https://www.indeed.com/jobs?q=junior&l=Orem%2C+UT&radius=25")
#     filename_indeed = 'output.txt'
#     with open(filename_indeed, 'w+') as f_obj:
#         f_obj.write(r.text)
#     pprint.pprint(r.text)

def parse_indeed(filepath):
    with open(filepath) as f_obj:
        soup = BeautifulSoup(f_obj, 'html.parser')
    jobs = soup.select(".jobsearch-SerpJobCard")
    jobs_list = []
    for job in jobs:
        job_dict = { "job_title" : '', "job_location": ''}
        job_title = job.select_one("h2 > a")
        try:
            job_dict['job_title'] = job_title['title']
        except TypeError:
            continue
        else:
            job_location_tag_list = job.select('.location')
            job_dict['job_location'] = job_location_tag_list[0].get_text()
            jobs_list.append(job_dict)
            # pprint.pprint(job_title)
            # pprint.pprint(job_location)
    return jobs_list
    

    # print(soup.prettify())
        

# retrieve_indeed()
entries = parse_indeed('output.txt')
for entry in entries:
    for key, value in entry.items():
        print(value)