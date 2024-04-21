import requests
import json
from pprint import pprint

api_url = "https://pxdata.stat.fi:443/PXWeb/api/v1/en/StatFin/icte/statfin_icte_pxt_13vg.px"

with open('query.json', 'r') as file:
    json_query = json.load(file)

response = requests.post(api_url, json=json_query)

# Check if the request was successful
if response.ok:
    # Parse JSON response
    data = response.json()
    pprint(data)

else:
    print("Failed to fetch data from API:", response.status_code)