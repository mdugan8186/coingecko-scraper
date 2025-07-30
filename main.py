# main.py

"""
Main script to fetch top cryptocurrencies from CoinGecko API and save to CSV.
"""

import csv
from modules.coingecko_api import get_top_100_cryptos
from modules.postprocess import clean_crypto_data
from pathlib import Path
from datetime import datetime
import json


timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
OUTPUT_PATH = Path(f"output/top_100_crypto_{timestamp}.csv")


def load_config(path="config.json"):
    """
    Loads configuration from a JSON file.
    """
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_fields(crypto_data):
    """
    Extracts relevant fields from each cryptocurrency entry.

    Parameters:
        crypto_data (list[dict]): Raw API data.

    Returns:
        list[dict]: Cleaned crypto records with selected fields.
    """
    cleaned = []

    for coin in crypto_data:
        cleaned.append({
            "Name": coin.get("name"),
            "Symbol": coin.get("symbol").upper(),
            "Current Price (USD)": coin.get("current_price"),
            "Market Cap": coin.get("market_cap"),
            "24h Volume": coin.get("total_volume"),
            "24h Price Change (%)": coin.get("price_change_percentage_24h"),
        })

    return cleaned


def save_to_csv(data, output_file):
    """
    Saves a list of dictionaries to a CSV file.

    Parameters:
        data (list[dict]): List of structured data records.
        output_file (str or Path): Path to the output CSV file.
    """
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def main():
    print("📡 Fetching data from CoinGecko API...")
    config = load_config()
    raw_data = get_top_100_cryptos(
        vs_currency=config["currency"],
        per_page=config["per_page"],
        page=config["page"]
    )

    if not raw_data:
        print("❌ No data fetched. Exiting.")
        return

    extracted_data = extract_fields(raw_data)
    cleaned_data = clean_crypto_data(extracted_data)
    save_to_csv(cleaned_data, OUTPUT_PATH)
    print(f"✅ Data saved to: {OUTPUT_PATH.resolve()}")


if __name__ == "__main__":
    main()
