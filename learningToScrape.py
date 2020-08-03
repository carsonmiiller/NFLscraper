import requests # for making standard html requests
from bs4 import BeautifulSoup # magical tool for parsing html data
import json # for parsing data
from pandas import DataFrame as df # premier library for data organization

page = requests.get("https://locations.familydollar.com/id/")
soup = BeautifulSoup(page.text, 'html.parser')
dollar_tree_list = soup.find_all(class_ = 'itemlist')
#example = dollar_tree_list[2] # a representative example
#example_content = example.contents
print(dollar_tree_list)