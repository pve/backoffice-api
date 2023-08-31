import requests
import os
from dotenv import load_dotenv
from urllib.parse import urljoin, urlencode
import time
import pandas as pd

# https://api.e-act.nl/api/apidocs/index.html

load_dotenv()
urlbase = "https://api.e-act.nl/api/1.0/"
params = {"admin": os.environ["AUTORESPOND_ADMIN_ID"], "key": os.environ["AUTORESPOND_API_KEY"]} 
headers = { "accept": "application/json" }

def get_groups():
    base_url = urlbase + "groups"

    page = 1
    total_pages = 1

    while page <= total_pages:
        
        url = urljoin(base_url, "?" + urlencode(params))

        response = requests.get(url, headers=headers)
        page += 1

        if response.status_code == 200:
            data = response.json().get("data")
        else:
            print(f"Error retrieving groups. Status code: {response.status_code}")
            return None

    return data

def get_users():
    base_url = urlbase + "groups/86755/relations"
# 86755,CCSK OL Foundation

    url = urljoin(base_url, "?" + urlencode(params))

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json().get("data")
    else:
        print(f"Error retrieving groups. Status code: {response.status_code}")
        return None

    return data

if __name__ == "__main__":
    groups = get_groups()
    users = get_users()

    if groups is not None:
        df = pd.DataFrame(groups)
        df.to_excel("reports/ar_groups_data.xlsx", index=False)
        df.to_csv("reports/ar_groups_data.csv", index=False)

    if users is not None:
        df = pd.DataFrame(users)
        df.to_excel("reports/ar_users_data.xlsx", index=False)
        df.to_csv("reports/ar_users_data.csv", index=False)