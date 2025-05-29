import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')
if not api_key:
    raise ValueError("API_KEY not found in environment variables")


url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={API_KEY}'
r = requests.get(url)
data = r.json()


print(data)