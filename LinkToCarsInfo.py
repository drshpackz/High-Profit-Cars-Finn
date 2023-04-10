import requests
from bs4 import BeautifulSoup
import csv
import re


def get_html(url):
    response = requests.get(url)
    return response.text

def is_ad_removed(html):
    soup = BeautifulSoup(html, 'html.parser')
    removed_text = 'Inaktiv'
    removed_element = soup.find(lambda tag: tag.name == 'div' and tag.get('class') == ['panel', 'u-pv0'] and removed_text in tag.text)
    return removed_element is not None

def extract_data(html, url):
    soup = BeautifulSoup(html, 'html.parser')

    # Extract car brand and model
    try:
        nav = soup.find('nav', {'class': 'finn-breadcrumbs-component'})
        car_brand = nav.find_all('a')[-2].text.strip()
        car_model = nav.find_all('a')[-1].text.strip()
    except AttributeError:
        car_brand = 'Unknown'
        car_model = 'Unknown'

    # Extract panel data
    try:
        section = soup.find('section', {'class': 'panel panel--bleed summary-icons'})
        data_divs = section.find_all('div', {'class': 'media__body'})

        data = {}
        for div in data_divs:
            key = div.find('div').text.strip()
            value = div.find('div', {'class': 'u-strong'}).text.strip()
            data[key] = value.replace('\xa0', ' ')
    except AttributeError:
        data = {}

    # Extract other fields
    fields = [
        'Omregistrering', 'Pris eks omreg', 'Farge', 'Interiørfarge', 'Hjuldrift', 'Effekt', 'Vekt',
        'Antall seter', 'Karosseri', 'Antall dører', 'Antall eiere', 'Avgiftsklasse',
        'Neste frist for EU-kontroll', 'Sylindervolum'
    ]

    for field in fields:
        try:
            field_div = soup.find('dt', string=field)
            if field_div:
                value = field_div.find_next_sibling('dd').text.strip()
                value = ' '.join(value.split())
                data[field] = value.replace('\xa0', ' ')
        except AttributeError:
            data[field] = 'Unknown'

    # Calculate total price
    try:
        omreg = int(re.sub(r'\D', '', data['Omregistrering'])) if data['Omregistrering'] else 0
        pris_eks = int(re.sub(r'\D', '', data['Pris eks omreg'])) if data['Pris eks omreg'] else 0
        total_sum = omreg + pris_eks
    except (KeyError, ValueError):
        total_sum = 'Unknown'

    # Skip Sylindervolum for electric cars
    if data.get('Drivstoff') == 'Elektrisitet':
        data['Sylindervolum'] = 'N/A'

    # Extract CarID
    try:
        car_id_div = soup.find('span', {'data-adid': True})
        car_id = car_id_div['data-adid']
    except AttributeError:
        car_id = 'Unknown'

    # Combine all data
    final_data = {
        'CarID': car_id,
        'Car_Brand': car_brand,
        'Car_Model': car_model,
        'Total_sum': total_sum,
        **data
    }

    # Remove Omregistrering and Pris eks omreg from final_data
    final_data.pop('Omregistrering', None)
    final_data.pop('Pris eks omreg', None)

    return final_data



def save_to_csv(data, filename):
    with open(filename, mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())
        writer.writerow(data)


def write_csv_header(filename, fieldnames):
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()


def main():
    filename = 'finncars.csv'
    print("Enter the URLs one per line. Enter 'q' to quit and parse the URLs:")

    urls = set()  # Use a set to store unique URLs
    while True:
        url = input()
        if url.lower() == 'q':
            break
        urls.add(url)  # Add the URL to the set

    if urls:
        # Write the CSV header using the first URL's data
        html = get_html(next(iter(urls)))
        if not is_ad_removed(html):
            data = extract_data(html, next(iter(urls)))
            write_csv_header(filename, data.keys())

        # Process all unique URLs
        for url in urls:
            html = get_html(url)
            if is_ad_removed(html):
                print(f"Ad removed from {url}")
                continue
            data = extract_data(html, url)
            save_to_csv(data, filename)
            print(f"Data saved from {url}")

if __name__ == '__main__':
    main()
