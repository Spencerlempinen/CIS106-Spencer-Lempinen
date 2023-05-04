import urllib.request
import re


def get_text(url):
    with urllib.request.urlopen(url) as response:
        text = response.read()
    return text


def get_tag_values(text, tag_name):
    tag_regex = re.compile(rf'<{tag_name}>(.+?)</{tag_name}>')
    tag_values = re.findall(tag_regex, text)
    return tag_values


def extract_cd_data(cd):
    title = re.search(r'<TITLE>(.*?)</TITLE>', cd).group(1)
    artist = re.search(r'<ARTIST>(.*?)</ARTIST>', cd).group(1)
    country = re.search(r'<COUNTRY>(.*?)</COUNTRY>', cd).group(1)
    price = float(re.search(r'<PRICE>(.*?)</PRICE>', cd).group(1))
    year = int(re.search(r'<YEAR>(.*?)</YEAR>', cd).group(1))
    return title, artist, country, price, year


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
    catalog_url = "https://www.w3schools.com/xml/cd_catalog.xml"
    titles, artists, countries, prices, years = read_catalog(catalog_url)
    display_catalog(titles, artists, countries, prices, years)
    calculate_avg(titles, prices)

main()
