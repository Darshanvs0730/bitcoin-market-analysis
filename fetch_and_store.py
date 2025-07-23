import requests
import pandas as pd
import os
from datetime import datetime

# Set up folder and file paths
folder_path = "data"
file_path = os.path.join(folder_path, "crypto_data.csv")

# Create folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print("✅ Created folder:", folder_path)

# Fetch Bitcoin price
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
response = requests.get(url)

if response.status_code == 200:
    price = response.json()["bitcoin"]["usd"]
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"✅ Bitcoin price fetched: ${price} at {now}")

    # Load existing data or create new
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        print("📄 Existing file loaded.")
    else:
        df = pd.DataFrame(columns=["Date", "Price"])
        print("🆕 New file will be created.")

    # Append new data
    new_row = {"Date": now, "Price": price}
    df.loc[len(df)] = new_row
    print("➕ Row added to dataframe:", new_row)

    # Save
    df.to_csv(file_path, index=False)
    print("💾 Data saved to", file_path)
else:
    print("❌ Failed to fetch price. Status code:", response.status_code)