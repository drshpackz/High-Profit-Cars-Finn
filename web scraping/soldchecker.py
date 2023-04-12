import pandas as pd
import requests
from bs4 import BeautifulSoup

# Load CSV data into a pandas DataFrame
df = pd.read_csv('cleaned_car_data.csv')

# Function to check if car is sold
def is_car_sold(finnkode):
    url = f'https://www.finn.no/car/used/ad.html?finnkode={finnkode}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    sold_tag = soup.find('span', class_='u-capitalize status status--warning u-mb0')
    if sold_tag and sold_tag.text.strip() == 'SOLGT':
        return True
    else:
        return False

# Add new column 'sold' to DataFrame
df['sold'] = df['CarID'].apply(is_car_sold)

# Save the updated DataFrame back to the CSV file
df.to_csv('cars_with_sold_status.csv', index=False)

# Print summary
num_cars = len(df)
num_sold = df['sold'].sum()
num_not_sold = num_cars - num_sold
print(f'Total cars: {num_cars}')
print(f'Sold cars: {num_sold}')
print(f'Unsold cars: {num_not_sold}')
