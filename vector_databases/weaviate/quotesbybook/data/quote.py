from bs4 import BeautifulSoup
import requests

import csv
import re

source = requests.get("https://quotesbybook.netlify.app/collections")

soup = BeautifulSoup(source.text, 'html.parser')

content = soup.body.find_all('div', class_="w-72 h-80 p-6 flex flex-col items-start gap-8 bg-white rounded-md shadow-md")

with open("data/quotesbybook.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Quote", "Author"])

    for _ in content:
        # find the quote and remove the quotes around them
        quote = re.sub(r'"', '', _.find("p").text.strip())
        # remove irregular spaces
        quote =  re.sub(r'\s+', ' ', quote)
        # find author and remove the -
        author = re.sub(r'-', '', _.find("div").text.strip())
        # load into csv
        csv_writer.writerow([author, quote])
