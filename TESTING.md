# Testing – CoinGecko API Scraper

## Sanity Flow
1. Run a scrape:
   ```bash
   python main.py
   ```
   - Confirms API request succeeds
   - Expects `output/coingecko_data.csv` (timestamped) to be created

2. Open CSV and verify columns:
   - `name, symbol, current_price, market_cap, volume_24h, price_change_24h_pct`

---

## Data Quality
- [ ] Prices (`current_price`) are numeric
- [ ] Market caps (`market_cap`) are numeric
- [ ] Volumes (`volume_24h`) are numeric
- [ ] 24h change is a percentage (float)
- [ ] No duplicate rows by `symbol`

---

## API Checks
- [ ] Endpoint URL is correct and live
- [ ] JSON response contains expected fields
- [ ] Rate limit (HTTP 429) handled gracefully
- [ ] Script retries on transient failures

---

## Optional Enhancements
- Add CLI flags for `--limit` (number of coins), `--out` (output path), and `--format` (csv/json)
- Add logging for API request/response status
- Add schema validation before saving CSV
- Add caching layer to avoid repeated API calls during testing

---

## Troubleshooting
- **Empty CSV**: Check API response in browser/postman; ensure endpoint is not down
- **429 Too Many Requests**: Wait and retry, or add rate limiting
- **Connection errors**: Increase timeout or retry logic
