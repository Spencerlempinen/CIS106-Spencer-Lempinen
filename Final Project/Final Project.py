# https://www.youtube.com/watch?v=sL64l9Aavpg&ab_channel=AVK47Python
# https://www.youtube.com/shorts/LjXBaYCvlhY
# https://www.youtube.com/watch?v=tlHNS-UTRIM&t=756s&ab_channel=NeuralNine
# Nick Rich(friend who does cloud security with CDW) :helped with the get_page_text function


import urllib.request
import re


def get_page_text(url):
    with urllib.request.urlopen(url) as response:
        page_text = response.read().decode('utf-8')
    return page_text


def get_tag_values(page_text, tag_name):
    tag_regex = re.compile(rf'<{tag_name}>(.*?)</{tag_name}>')
    tag_values = re.findall(tag_regex, page_text)
    return tag_values


def get_cd_data(page_text):
    titles = get_tag_values(page_text, "TITLE")
    artists = get_tag_values(page_text, "ARTIST")
    countries = get_tag_values(page_text, "COUNTRY")
    prices = [float(p) for p in get_tag_values(page_text, "PRICE")]
    years = [int(y) for y in get_tag_values(page_text, "YEAR")]
    return titles, artists, countries, prices, years


def calculate_avg(prices):
    num_items = len(prices)
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
    page_text = get_page_text(catalog_url)
    titles, artists, countries, prices, years = get_cd_data(page_text)
    display_catalog(titles, artists, countries, prices, years)
    calculate_avg(prices)


main()

