import requests
import re
import csv
from bs4 import BeautifulSoup

def parse_car_data(finnkode):
    url = f'https://www.finn.no/car/used/ad.html?finnkode={finnkode}'

    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')

    script = soup.find_all('script')[3].text.strip()[5:-2]

    brand = re.search(r'"merke":\s*"(\w+)"', script)
    if brand:
        brand = brand.group(1)

    model = re.search(r'"(?:model|modell)":\s*"([\w-]+)"', script)
    if model:
        model = model.group(1)

    price = re.search(r'"pris":\s*"([\d\s]+)",', script)
    if price:
        price = price.group(1)

    weight = re.search(r'"vekt":\s*"([\d\s]+)",', script)
    if weight:
        weight = weight.group(1)
    else:
        weight_element = soup.select_one("section.panel dt:-soup-contains('Vekt') + dd")
        if weight_element:
            weight = weight_element.text.strip()

    frame = re.search(r'"ramme":\s*"([\w-]+)"', script)
    if frame:
        frame = frame.group(1)
    else:
        frame_element = soup.select_one("section.panel dt:-soup-contains('Karosseri') + dd")
        if frame_element:
            frame = frame_element.text.strip()

    seats = re.search(r'"seter":\s*"([\d\s]+)",', script)
    if seats:
        seats = seats.group(1)
    else:
        seats_element = soup.select_one("section.panel dt:-soup-contains('Antall seter') + dd")
        if seats_element:
            seats = seats_element.text.strip()

    code = re.search(r'"finnkode":\s*"(\d+)",', script)
    if code:
        code = code.group(1)

    gearbox = re.search(r'"girkasse":\s*"([\w\s]+)"', script)
    if gearbox:
        gearbox = gearbox.group(1)
    else:
        gearbox_element = soup.select_one("section.panel dt:-soup-contains('Gir') + dd")
        if gearbox_element:
            gearbox = gearbox_element.text.strip()

    year = re.search(r'"aarsmodell":\s*"(\d+)"', script)
    if year:
        year = year.group(1)
    else:
        year_element = soup.select_one("section.panel dt:-soup-contains('1. gang registrert') + dd")
        if year_element:
            year = year_element.text.strip()

    hk = re.search(r'"hestekrefter":\s*"(\d+)"', script)
    if hk:
        hk = hk.group(1)
    else:
        hk_element = soup.select_one("section.panel dt:-soup-contains('Effekt') + dd")
        if hk_element:
            hk = hk_element.text.strip().split()[0]

    variant = re.search(r'"variant":\s*"([\w\s\.\-]+)"', script)
    if variant:
        variant = variant.group(1)
    else:
        variant_element = soup.select_one("div.panel h1 + p")
        if variant_element:
            variant = variant_element.text.strip()
        else:
            variant = "Unknown"

    car_data = [code, brand, model, price, weight.replace('\xa0', ' '), frame, seats, gearbox, year, hk, variant]
    missing_data = []

    for index, data in enumerate(car_data):
        if not data:
            missing_data.append(index)

    if not missing_data:
        with open('car_data.csv', mode='a+', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(car_data)
        print(f"Data for Car ID {finnkode} successfully imported and written to CSV file.")
    else:
        data_labels = ['CarID', 'Brand', 'Model', 'Price', 'Weight', 'Frame', 'Seats', 'Gearbox', 'Year', 'hk', 'Variant']
        missing_labels = [data_labels[i] for i in missing_data]
        print(
            f"Data for Car ID {finnkode} not written to CSV file due to missing information: {', '.join(missing_labels)}")


print("Enter car IDs one per line, then type 'q' to start parsing:")

car_ids = []
while True:
    car_id = input()
    if car_id == 'q':
        break
    car_ids.append(car_id)

with open('car_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    csv_header = ['CarID', 'Brand', 'Model', 'Price', 'Weight', 'Frame', 'Seats', 'Gearbox', 'Year', 'hk', 'Variant']
    writer.writerow(csv_header)

for car_id in car_ids:
    parse_car_data(car_id)
