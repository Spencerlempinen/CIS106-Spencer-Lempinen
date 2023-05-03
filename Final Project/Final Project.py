import re
import requests

def read_catalog(url):
    titles = []
    artists = []
    countries = []
    prices = []
    years = []

    response = requests.get(url)
    if response.status_code != 200:
        print(f"failed to retrieve data from {url}")
        return titles

    cd_regex = re.compile(r'<CD>(.+?)</CD>', re.DOTALL)
    cds = re.findall(cd_regex, response.text)

    for cd in cds:
        title = re.search(r'<TITLE>(.+?)</TITLE>', cd).group(1)
        artist = re.search(r'<ARTIST>(.+?)</ARTIST>', cd).group(1)
        country = re.search(r'<COUNTRY>(.+?)</COUNTRY', cd).group(1)
        price = float(re.search(r'<PRICE>(.+?)</PRICE>', cd).group(1))
        year = int(re.search(r'<YEAR>(.+?)</YEAR>', cd).group(1))
        titles.append(title)
        artists.append(artist)
        countries.append(country)
        prices.append(price)
        years.append(year)

    return titles, artists, countries, prices, years

def display_output(titles, artists, countries, prices, years):
    for i in range(len(titles)):
        print(f"{titles[i]} - {artists[i]} - {countries[i]} - ${prices[i]:.2f} - {years[i]}")

def main():
    url = "https://www.w3schools.com/xml/cd_catalog.xml"
    titles, artists, countries, prices, years = read_catalog(url)
    display_output(titles, artists, countries, prices, years)

main()
