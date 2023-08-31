import requests
import os
from dotenv import load_dotenv
from urllib.parse import urljoin, urlencode
import time
import pandas as pd

# https://docs.teachable.com/reference/

load_dotenv()
urlbase = "https://developers.teachable.com/v1/"

def get_users():
    base_url = urlbase + "users"
    headers = {
        "accept": "application/json",
        "apiKey": os.environ["TEACHABLE_API_KEY"]
    }

    users = []
    page = 1
    total_pages = 1

    while page <= total_pages:
        params = {"page": page, "per": 20}
        url = urljoin(base_url, "?" + urlencode(params))

        response = requests.get(url, headers=headers)
        # rate limit = 360 /minute, could be smarter.
        time.sleep(0.2)

        if response.status_code == 200:
            data = response.json()

            # Check if the "users" key is present in the JSON response
            if "users" in data:
                users.extend(data["users"])
                page += 1

                meta = data.get("meta")
                if meta:
                    total_pages = meta.get("number_of_pages", 1)
                else:
                    break
            else:
                print("Invalid JSON response. The 'users' key is missing.")
                return None
        else:
            print(f"Error retrieving users. Status code: {response.status_code}")
            return None

    return users

def get_enrollments(courseid):
    base_url = urlbase + "courses/" + courseid + "/enrollments"
    headers = {
        "accept": "application/json",
        "apiKey": os.environ["TEACHABLE_API_KEY"]
    }

    enrollments = []
    page = 1
    total_pages = 1

    while page <= total_pages:
        params = {"page": page, "per": 20}
        url = urljoin(base_url, "?" + urlencode(params))
#        url = 'https://developers.teachable.com/v1/courses/265372/enrollments'
        response = requests.get(url, headers=headers)
        # rate limit = 360 /minute, could be smarter.
        time.sleep(0.2)

        if response.status_code == 200:
            data = response.json() # more in response.text

            # Check if the "enrollments" key is present in the JSON response
            if "enrollments" in data:
                enrollments.extend(data["enrollments"])
                page += 1

                meta = data.get("meta")
                if meta:
                    total_pages = meta.get("number_of_pages", 1)
                else:
                    break
            else:
                print("Invalid JSON response. The 'enrollments' key is missing.")
                return None
        else:
            print(f"Error retrieving enrollments. Status code: {response.status_code}")
            return None

    return enrollments

if __name__ == "__main__":
    enrollments = get_enrollments("265372") # CASA
    if enrollments is not None:
        dfe = pd.DataFrame(enrollments).drop_duplicates(subset=['user_id']) #still not unique?
#        df = pd.DataFrame(enrollments)
#        dfe = df[df.duplicated('user_id', keep=False)]['user_id'].unique()
#        dfe = df[df.duplicated('user_id', keep='first')]
        dfe.to_csv("teachable_enrollments_data.csv", index=False)
        dfe.to_excel("teachable_enrollments_data.xlsx", index=False)
    users = get_users()
    if users is not None:
        dfu = pd.DataFrame(users).rename(columns={'id':'user_id'}).drop_duplicates(subset=['user_id']) 
        dfu.to_csv("teachable_users_data.csv", index=False)
        dfu.to_excel("teachable_users_data.xlsx", index=False)
        combined = pd.merge(dfe, dfu, how = 'inner', on='user_id', validate='1:1')
#        dfe.merge(dfu, how = 'inner', on='user_id', validate='1:1')
        combined.to_csv("teachable_useremail_data.csv", index=False)
        i=1

