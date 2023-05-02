import re
import requests


def read_catalog(url):
    titles = []

    response = requests.get
    if response.status_code != 200:
        print(f"failed to retrive data from {url}")
        return titles

    cd_regex = re.compile(r'<CD>(.*?)</CD>', re.DOTALL)
    cds = re.findall(cd_regex, response.text)

    for cd in cds:
        title = re.find(r'<TITLE>(.*?)<TITLE>', cd).group(1)
        titles.append(title)
    return titles

def display_output(titles):
    for i in range(len(titles)):
        print(f"titles[i]")


def main():
    url = "https://www.w3schools.com/xml/cd_catalog.xml"
    titles = read_catalog(url)
    display_output(titles)
