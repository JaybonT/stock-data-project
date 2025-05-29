import requests
import os
import logging
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')
if not api_key:
    raise ValueError("API_KEY not found in environment variables")

def fetch_stock_data(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={api_key}'
    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
        if 'Error Message' in data:
            logging.error(f"Error fetching data for {symbol}: {data['Error Message']}")
            return None
        if 'Note' in data:
            logging.warning(f"API limit reached: {data['Note']}")
            return None
        return data
    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")
        return None
