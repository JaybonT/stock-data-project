import json
import boto3
import time
import pandas as pd
from datetime import datetime
from api.alphavantage import fetch_stock_data

def upload_raw_json_to_s3(symbol, bucket_name):
    raw_data = fetch_stock_data(symbol)
    s3 = boto3.client('s3')
    date_str = datetime.utcnow().strftime("%Y-%m-%d")
    s3.put_object(
        Bucket=bucket_name,
        Key=f"raw/{symbol}_raw_{date_str}.json",
        Body=json.dumps(raw_data),
        ContentType="application/json"
    )

if __name__ == "__main__":
    # Read symbols from CSV
    symbols_df = pd.read_csv("data/sp500.csv")
    symbols = symbols_df['Symbol'].dropna().unique()
    for symbol in symbols:
        print(f"Uploading data for {symbol}...")
        upload_raw_json_to_s3(symbol, "stock-data-raw-jasontran")
        time.sleep(12)  # Wait 12 seconds between requests
    print("All stock data uploaded.")