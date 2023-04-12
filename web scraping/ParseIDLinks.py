import requests
from bs4 import BeautifulSoup
import csv
import re

def get_car_ids_from_url(url):
    car_ids = []
    page = 1
    while True:
        if "&page=" in url:
            url_with_page = re.sub(r"&page=\d+", f"&page={page}", url)
        else:
            url_with_page = f"{url}&page={page}"

        response = requests.get(url_with_page)
        soup = BeautifulSoup(response.text, 'html.parser')

        error_div = soup.find("div", class_="panel u-text-center u-mv64")
        if error_div:
            break

        articles = soup.find_all("article", class_="ads__unit")

        if not articles:
            break

        for article in articles:
            car_id_element = article.find("a", class_="ads__unit__link")
            if car_id_element:
                car_id = car_id_element.get("id")
                if car_id:
                    car_ids.append(car_id)

        page += 1

    return car_ids

def main():
    urls = input("Enter the URLs separated by spaces: ").split()
    all_car_ids = []

    for url in urls:
        car_ids = get_car_ids_from_url(url)
        all_car_ids.extend(car_ids)

    with open("car_ids.csv", "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Car ID"])

        for car_id in all_car_ids:
            csvwriter.writerow([car_id])

    print("Car IDs saved to car_ids.csv")

if __name__ == "__main__":
    main()
##ITS ACTUALLY PARSE ID OF CARS BY INSERTING SEPARATED BY SPACES WORKS GOOD!!!!
