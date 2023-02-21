# --- Syllabi Scraper ---
# Authors: Nakul Bansal, Micah Baker

import requests                # Python requests module: for POSTing and GETing
from bs4 import BeautifulSoup  # Beautiful Soup module: for parsing webpages
from time import sleep

INTERVAL = 0.01

def scraper(test=None):
    # The URL of the course portal
    url = 'http://www.sfu.ca/bin/wcm/course-outlines'

    # The year to check for
    year = 2022

    # Keywords to search for
    keywords = [ 'chatgpt', 'openai' ]

    terms = requests.get(f'{url}?{year}').json()

    for term in terms:
        t = term['text']

        depts = requests.get(f'{url}?{year}/{t}')

        if depts.status_code != 200:
            continue

        for dept in depts.json():
            d = dept['text']

            courses = requests.get(f'{url}?{year}/{t}/{d}')

            if courses.status_code != 200:
                continue

            for course in courses.json():
                c = course['text']

                sections = requests.get(f'{url}?{year}/{t}/{d}/{c}')

                if sections.status_code != 200:
                    continue

                for section in sections.json():
                    s = section['text']

                    outline_get = requests.get(f'{url}?{year}/{t}/{d}/{c}/{s}')

                    if outline_get.status_code != 200:
                        continue;

                    outline = outline_get.json()
                    search = str(outline).lower()

                    for keyword in keywords:
                        if keyword in search:
                            print(f'\t!!! FOUND {keyword} in {year}/{t}/{d}/{c}/{s}')

                            with open('log.txt', 'a') as log:
                                log.write(f'{keyword}: {url}?{year}/{t}/{d}/{c}/{s}\n')

                print(f'({c})', end='', flush=True)
            
            print(f'\nChecked {url}?{year}/{t}/{d}.') 

    print('All done.')

if __name__ == '__main__':
    scraper()
