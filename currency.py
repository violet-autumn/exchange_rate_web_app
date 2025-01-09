import requests
import os

# Call the API to get today's currency exchange rates for the base currency

def get_currency_rate(base_currency="USD"):
    request_url=f'https://open.er-api.com/v6/latest/{base_currency}'
    currency_data = requests.get(request_url).json()
    return currency_data
