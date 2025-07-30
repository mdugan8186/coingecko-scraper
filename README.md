# CoinGecko Cryptocurrency Scraper

Fetch the top 100 cryptocurrencies by market cap from the CoinGecko public API and export structured, cleaned data to CSV. This script is built as a modular, production-ready Python scraper for portfolio and freelance use.

---

## 📌 Features

- Retrieves top cryptocurrencies using the [CoinGecko API](https://www.coingecko.com/en/api/documentation)
- Extracts key metrics:
  - Name
  - Symbol
  - Current Price (USD)
  - Market Cap
  - 24h Volume
  - 24h Price Change (%)
- Cleans and formats data (e.g., rounding, comma formatting)
- Saves results to a timestamped CSV in the `output/` folder
- Loads configurable parameters from `config.json`
- Sample cleaned output provided for preview

---

## ⚙️ Configuration

You can customize the request using `config.json`:

```json
{
  "currency": "usd",
  "per_page": 100,
  "page": 1
}
```

Change the `"currency"` field to `"eur"`, `"btc"`, etc. as supported by the CoinGecko API.

---

## 🚀 Usage

1. Clone the repository:

```bash
git clone https://github.com/mdugan8186/coingecko-scraper.git
cd coingecko-scraper
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the script:

```bash
python3 main.py
```

4. Find the output CSV in the `output/` folder with a timestamped filename like:

```
top_100_crypto_2025-07-29_22-38-18.csv
```

---

## 📂 Project Structure

```
coingecko-scraper/
├── main.py
├── config.json
├── modules/
│   ├── coingecko_api.py
│   └── postprocess.py
├── output/
│   └── top_100_crypto_<timestamp>.csv
├── samples/
│   └── sample_output.csv
├── requirements.txt
└── README.md
```

---

## 📊 Sample Output

Preview the cleaned data format in:

📁 `samples/sample_output.csv`

---

## 🧰 Technologies Used

- Python 3.13
- `requests` for API calls
- Standard libraries (`csv`, `json`, `pathlib`)
- Modular file structure for maintainability

---

## 👨‍💻 Author

**Michael Dugan**  
Built for portfolio and freelance demonstration.  
GitHub: [mdugan8186](https://github.com/mdugan8186)

---

## 📝 License

This project is open-source and free to use for educational or personal use.
