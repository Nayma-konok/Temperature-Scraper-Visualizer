import requests
import selectorlib
from datetime import datetime


URL= "https://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/39.0.2171.95 Safari/537.36'}

def scrape(url):
    """scrape the page source from the URL"""
    response=requests.get(url, headers=HEADERS)
    return response.text 

def extract(source):
    extractor=selectorlib.Extractor.from_yaml_file("extract1.yaml")
    value=extractor.extract(source)["tours"]
    return value

def read_file():
    """Read data.txt and return list of existing events"""
    try:
        with open("temp_data.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []
    
if __name__=="__main__":
        scraped=scrape(URL)
        temperature=extract(scraped)
        print(temperature)

        existing_events = read_file()
        if temperature not in existing_events:
            now = datetime.now()
            dates = now.strftime("%Y-%m-%d %H:%M:%S")
            entry = f"{dates} , {temperature}"
            with open("temp_data.txt", "a") as file:
                file.write(entry + "\n") 