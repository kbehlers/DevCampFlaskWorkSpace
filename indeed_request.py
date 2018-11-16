import requests
import pprint
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin, quote_plus, urlencode


def retrieve_indeed(search_term):
    encoded_search_term = quote_plus(search_term)
    print(encoded_search_term)
    r = requests.get(f"https://www.indeed.com/jobs?q={encoded_search_term}&l=")
    filename_indeed = 'output.txt'
    with open(filename_indeed, 'w+') as f_obj:
        f_obj.write(r.text)
    return parse_indeed(filename_indeed)
    # pprint.pprint(r.text)

def parse_indeed(filepath):
    with open(filepath) as f_obj:
        soup = BeautifulSoup(f_obj, 'html.parser')
    #Grab each job card on page
    jobs = soup.select(".jobsearch-SerpJobCard")
    jobs_list = []

    for job in jobs:
        job_dict = { "job_title" : '', "job_location": '', "job_link": '', 'job_company': '', 'job_summary': ''}
        job_title = job.select_one("h2 > a")
        try:
            #Test to see if job card has a title
            job_dict['job_title'] = job_title['title']
        except TypeError:
            #If there isn't a job title, don't bother trying other attributes
            continue
        else:
            job_link_base_url = "https://www.indeed.com"
            job_link_suffix = job_title['href']
            job_link_complete_url = urljoin(job_link_base_url, job_link_suffix)
            job_dict['job_link'] = job_link_complete_url
            job_location_tag_list = job.select('.location')
            job_dict['job_location'] = job_location_tag_list[0].get_text()
            job_summary_tag_list = job.select('.summary')
            job_dict['job_summary'] = job_summary_tag_list[0].get_text().strip()
            job_company_tag_list = job.select('.company')
            job_dict['job_company'] = job_company_tag_list[0].get_text().strip()

            #Update jobs_list with parsed attributes
            jobs_list.append(job_dict)

    return jobs_list
        

# retrieve_indeed()
# entries = parse_indeed('output.txt')
# for entry in entries:
#     for key, value in entry.items():
#         print(value)