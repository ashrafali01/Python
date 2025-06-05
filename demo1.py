import requests
import pandas as pd

# TfL Bus Stop ID (e.g., Oxford Circus)
stop_id = "490008660N"

# Optionally add your app_id and app_key
app_id = ""     # Optional
app_key = ""    # Optional

url = f"https://api.tfl.gov.uk/StopPoint/{stop_id}/Arrivals"

params = {}
if app_id and app_key:
    params = {"app_id": app_id, "app_key": app_key}

response = requests.get(url, params=params)

if response.status_code == 200:
    arrivals = response.json()
    df = pd.DataFrame(arrivals)
    print(df[['lineName', 'destinationName', 'expectedArrival', 'timeToStation']])
else:
    print(f"Error: {response.status_code}")

