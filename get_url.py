# This program collects all urls of a given website using regular expression and saves them in a csv file
import requests
import re

url = "https://books.toscrape.com/"

r = requests.get(url)

data = r.text
url_pattern = re.compile('<a href="(.*?)"')
res = re.findall(url_pattern, data)

with open("href.csv", "w") as f:
    for i in res:
        f.write(i + "\n")
    f.close()