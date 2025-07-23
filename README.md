📈 Bitcoin Market Analysis Using Automated ETL and Time-Series Techniques
A data-driven project that automatically collects, processes, and analyzes Bitcoin (BTC) price data every 15 minutes using a custom ETL pipeline and time-series visualizations.

🚀 Features
✅ Automated Data Fetching: Real-time BTC prices are fetched every 15 minutes using a scheduled cron job.

✅ ETL Pipeline: Fetched data is stored in a structured CSV format for continuous growth and reusability.

✅ Time-Series Analysis: Jupyter Notebook loads live CSV data and visualizes trends using moving averages (SMA-20), OHLC charts, and volatility insights.

✅ Data Visualizations: Uses Python libraries like Matplotlib and Seaborn to generate clean, informative charts.

✅ Cron Integration: Linux/macOS cron job ensures automated data collection without manual intervention.

🛠️ Tech Stack
Python

- Pandas
- Matplotlib
- Jupyter Notebook
- Seaborn
- Cron (macOS)


⚙️ How It Works:
fetch_and_store.py fetches the latest BTC price from CoinGecko API.

Saves the timestamped price in data/crypto_data.csv.

Cron runs this script every 15 minutes.

The Jupyter notebook automatically loads the updated CSV for real-time analysis and plotting.

📊 Sample Charts & Insights:
SMA-20 Line Graph

Volatility & Trend Patterns

OHLC Candlestick Charts (optional)

🧠 Concepts Applied
ETL (Extract, Transform, Load)

Time-Series Analysis

Moving Averages

Real-time Data Monitoring

Automation with Cron