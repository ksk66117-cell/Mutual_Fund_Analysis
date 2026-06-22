import requests
import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

funds = {
    "HDFC_Top100_Direct": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, code in funds.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        json_data = response.json()

        meta_data = json_data["meta"]
        nav_data = json_data["data"]

        df = pd.DataFrame(nav_data)

        filename = f"data/raw/{fund_name}.csv"

        df.to_csv(filename, index=False)

        print(f"{fund_name} saved successfully")

    else:
        print(f"Unable to fetch {fund_name}")