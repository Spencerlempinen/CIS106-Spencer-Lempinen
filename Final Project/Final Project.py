import re
import requests

def read_catalog(url):
    titles = []
    artists = []
    countries = []

    response = requests.get(url)
    if response.status_code != 200:
        print(f"failed to retrieve data from {url}")
        return 

    cd_regex = re.compile(r'<CD>(.+?)</CD>', re.DOTALL)
    cds = re.findall(cd_regex, response.text)

    for cd in cds:
        title = re.search(r'<TITLE>(.+?)</TITLE>', cd).group(1)
        artist = re.search(r'<ARTIST>(.+?)</ARTIST>', cd).group(1)
        country = re.search(r'<COUNTRY>(.+?)</COUNTRY', cd).group(1)
        titles.append(title)
        artists.append(artist)
        countries.append(country)

    return titles, artists, countries

def display_output(titles, artists, countries):
    for i in range(len(titles)):
        print(titles[i] + " - " + artists[i] + " - " + countries[i])

def main():
    url = "https://www.w3schools.com/xml/cd_catalog.xml"
    titles, artists, countries = read_catalog(url)
    display_output(titles, artists, countries)

main()
