# --- Syllabi Scraper ---
# Authors: Nakul Bansal, Micah Baker

from bs4 import BeautifulSoup

html_doc = "<doctype! html></html>"

soup = BeautifulSoup(html_doc, 'html.parser')
