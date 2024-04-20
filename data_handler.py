import requests
import json

api_url = "https://pxdata.stat.fi/PXWeb/api/v1/en/StatFin/icte/statfin_icte_pxt_13vg.px"

with open('query.json', 'r') as file:
    json_query = json.load(file)

response = requests.post(api_url, json=json_query)

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON response
    data = response.json()

    # Now you can work with the JSON data
    # For example, you can print the entire JSON data
    print(json.dumps(data, indent=4))
else:
    print("Failed to fetch data from API:", response.status_code)