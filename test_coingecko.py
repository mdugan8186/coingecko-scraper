# test_coingecko.py (temporary test file)

from modules.coingecko_api import get_top_100_cryptos
import json

data = get_top_100_cryptos()
print(json.dumps(data[:2], indent=2))  # Show first 2 entries for inspection
