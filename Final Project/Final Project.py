# References:
# https://www.youtube.com/watch?v=sL64l9Aavpg&ab_channel=AVK47Python
# https://www.youtube.com/shorts/LjXBaYCvlhY
# https://www.youtube.com/watch?v=tlHNS-UTRIM&t=756s&ab_channel=NeuralNine
# Nick Rich(friend who does cloud security with CDW) :helped with the get_page_text function
# co-pilot


import urllib.request
import re


def get_text(url):
    try:
        with urllib.request.urlopen(url) as response:
            text = response.read().decode('utf-8')
            if not text:
                return ValueError("Error: file missing")
            return text
    except urllib.error.URLError as e:
        return ValueError(f"Failed to retrieve data from {url}: {e}")


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


def display_catalog(titles, artists, countries, prices, years, num_items_to_display=None):
    num_items = len(titles)
    if num_items == 0:
        return ValueError("Error: missing or incorrect data")
    if num_items_to_display is not None and num_items_to_display < num_items:
        num_items = num_items_to_display
    print("title - artist - country - price - year")
    for i in range(num_items):
        print(f"{titles[i]} - {artists[i]} - {countries[i]} - ${prices[i]:.2f} - {years[i]}")


def main():
    catalog_url = "https://www.w3schools.com/xml/cd_catalog.xml"
    page_text = get_text(catalog_url)
    titles, artists, countries, prices, years = get_cd_data(page_text)
    display_catalog(titles, artists, countries, prices, years)
    calculate_avg(prices)


main()
