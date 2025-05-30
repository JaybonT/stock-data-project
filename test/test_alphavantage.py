import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/api')))

from alphavantage import fetch_stock_data # type: ignore

if __name__ == "__main__":
    symbol = input("Enter stock symbol (e.g., IBM): ").upper()
    data = fetch_stock_data(symbol)
    print(data)