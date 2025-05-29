import pandas as pd
from api.alphavantage import fetch_stock_data
import logging

def load_intraday_data(symbol):
    """
    Retrieve and process intraday stock data for a given symbol from Alpha Vantage.
    Returns a DataFrame with standardized column names and proper data types.
    """
    response = fetch_stock_data(symbol)
    if not response or "Time Series (5min)" not in response:
        logging.error(f"Failed to retrieve data for {symbol}.")
        raise ValueError(f"No data available for {symbol}.")

    time_series = response["Time Series (5min)"]
    records = []
    for timestamp, values in time_series.items():
        record = {
            "timestamp": pd.to_datetime(timestamp),
            "open": float(values.get("1. open", 0)),
            "high": float(values.get("2. high", 0)),
            "low": float(values.get("3. low", 0)),
            "close": float(values.get("4. close", 0)),
            "volume": float(values.get("5. volume", 0))
        }
        records.append(record)
    df = pd.DataFrame(records)
    df = df.sort_values("timestamp").set_index("timestamp")
    return df