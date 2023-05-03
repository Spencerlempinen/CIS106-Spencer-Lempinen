import requests
import re


def extract_cd_data(cd):
    title = re.search(r'<TITLE>(.*?)</TITLE>', cd).group(1)
    artist = re.search(r'<ARTIST>(.*?)</ARTIST>', cd).group(1)
    country = re.search(r'<COUNTRY>(.*?)</COUNTRY>', cd).group(1)
    price = float(re.search(r'<PRICE>(.*?)</PRICE>', cd).group(1))
    year = int(re.search(r'<YEAR>(.*?)</YEAR>', cd).group(1))
    return title, artist, country, price, year


def read_catalog(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve data from {url}")
        return None
    else:
        titles = []
        artists = []
        countries = []
        prices = []
        years = []
        cd_regex = re.compile(r'<CD>(.*?)</CD>', re.DOTALL)
        cds = re.findall(cd_regex, response.text)

        for cd in cds:
            cd_data = extract_cd_data(cd)
            title, artist, country, price, year = cd_data
            titles.append(title)
            artists.append(artist)
            countries.append(country)
            prices.append(price)
            years.append(year)
        return titles, artists, countries, prices, years


def calculate_avg(titles, prices):
    num_items = len(titles)
    if num_items == 0:
        return None
    else:
        total_price = sum(prices)
        avg_price = total_price / num_items
        return print(f"{num_items} items - ${avg_price:.2f} average price")


def display_catalog(titles, artists, countries, prices, years):
    if len(titles) == 0:
        print("Error: missing or bad data")
        return None
    else:
        print("title - artist - country - price - year")
        for i in range(len(titles)):
            print(f"{titles[i]} - {artists[i]} - {countries[i]} - ${prices[i]:.2f} - {years[i]}")


def main():
    catalog_url = "https://www.w3schools.com/xml/plant_catalog.xml"
    titles, artists, countries, prices, years = read_catalog(catalog_url)
    display_catalog(titles, artists, countries, prices, years)
    calculate_avg(titles, prices)


main()
