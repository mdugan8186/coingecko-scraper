# modules/postprocess.py

"""
Utility functions for postprocessing and cleaning CoinGecko data.
"""


def clean_crypto_data(data):
    """
    Cleans the extracted crypto data.

    - Rounds numerical values
    - Formats large numbers with commas
    - Removes entries missing key fields

    Parameters:
        data (list[dict]): Raw list of extracted records

    Returns:
        list[dict]: Cleaned list of records
    """
    cleaned = []

    for record in data:
        try:
            cleaned.append({
                "Name": record["Name"],
                "Symbol": record["Symbol"],
                "Current Price (USD)": round(record["Current Price (USD)"], 2),
                "Market Cap": f'{int(record["Market Cap"]):,}',
                "24h Volume": f'{int(record["24h Volume"]):,}',
                "24h Price Change (%)": round(record["24h Price Change (%)"], 2),
            })
        except (KeyError, TypeError, ValueError):
            # Skip rows with missing or invalid values
            continue

    return cleaned
