# modules/coingecko_api.py

"""
CoinGecko API interface for retrieving cryptocurrency data.
"""

import requests


def get_top_100_cryptos(vs_currency="usd", per_page=100, page=1):
    """
    Fetch the top cryptocurrencies by market cap using the CoinGecko API.

    Parameters:
        vs_currency (str): The fiat currency to convert values into (e.g., 'usd').
        per_page (int): Number of coins to fetch per page (max 250).
        page (int): Page number of results (start with 1).

    Returns:
        list[dict]: List of cryptocurrency data dictionaries.
    """
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": vs_currency,
        "order": "market_cap_desc",
        "per_page": per_page,
        "page": page,
        "sparkline": False,
        "price_change_percentage": "24h",
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.RequestException as e:
        print(f"❌ Error fetching data from CoinGecko: {e}")
        return []
