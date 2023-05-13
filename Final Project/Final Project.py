# This program will process and XMl file from a URL and parse it,
# and return the average price and the list of CDS

# References:
# https://www.youtube.com/watch?v=sL64l9Aavpg&ab_channel=AVK47Python
# https://www.youtube.com/shorts/LjXBaYCvlhY
# https://www.youtube.com/watch?v=tlHNS-UTRIM&t=756s&ab_channel=NeuralNine
# https://www.youtube.com/watch?v=K8L6KVGG-7o&ab_channel=CoreySchafer
# Nick Rich(does cloud security with CDW): helped w/ the get_page_text
# co-pilot


import urllib.request
import re

# I added this module becuase im currently out of town working on my MacBook 
# this was the only way I could get the code I was working on to output anything im not sure why but this made it work
import ssl
ssl._create_default_https_context = ssl._create_unverified_context



def get_text(url):
    try:
        with urllib.request.urlopen(url) as response:
            content_type = response.headers.get('Content-Type', '')
            if 'xml' not in content_type:
                raise ValueError(f"Error: {url} does not contain an XML file")
            text = response.read().decode('utf-8')
            if not text:
                raise ValueError("Error: file is empty")
            return text
    except urllib.error.HTTPError as e:
        if e.code == 404:
            raise ValueError(f"Error 404: File not found at {url}")
        else:
            raise ValueError(f"Failed to retrieve data from {url}: {e}")
    except urllib.error.URLError as e:
        raise ValueError(f"Failed to retrieve data from {url}: {e}")


def get_tag_values(text, tag):
    tag_regex = re.compile(fr'<{tag}>(.*?)</{tag}>', re.DOTALL)
    tag_matches = re.findall(tag_regex, text)
    if not tag_matches:
        return ValueError("Error: missing or incorrect data")
    tag_values = []
    for match in tag_matches:
        if not match.strip():
            return ValueError("Error: missing or incorrect data")
        tag_values.append(match.strip())
    return tag_values


def get_cd_data_titles(page_text):
    titles = get_tag_values(page_text, "TITLE")
    return titles


def get_cd_data_artists(page_text):
    artists = get_tag_values(page_text, "ARTIST")
    return artists


def get_cd_data_countries(page_text):
    countries = get_tag_values(page_text, "COUNTRY")
    return countries


def get_cd_data_prices(page_text):
    prices = [float(p) for p in get_tag_values(page_text, "PRICE")]
    return prices


def get_cd_data_years(page_text):
    years = [int(y) for y in get_tag_values(page_text, "YEAR")]
    return years


def calculate_avg(prices):
    num_items = len(prices)
    if num_items == 0:
        return None
    else:
        total_price = sum(prices)
        avg_price = total_price / num_items
        return print(f"{num_items} items - ${avg_price:.2f} average price")


def display_catalog(titles, artists, countries, prices, years):
    num_items = len(titles)
    if num_items == 0:
        return ValueError("Error: missing or incorrect data")
    print("title - artist - country - price - year")
    for i in range(num_items):
        print(f"{titles[i]} - {artists[i]} - "
              f"{countries[i]} - ${prices[i]:.2f} - {years[i]}")


def main():
    catalog_url = "https://www.w3schools.com/xml/cd_catalog.xml"
    page_text = get_text(catalog_url)
    titles = get_cd_data_titles(page_text)
    artists = get_cd_data_artists(page_text)
    countries = get_cd_data_countries(page_text)
    prices = get_cd_data_prices(page_text)
    years = get_cd_data_years(page_text)
    display_catalog(titles, artists, countries, prices, years)
    calculate_avg(prices)


main()
