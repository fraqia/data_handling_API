import requests
import json
import sys

# api_url = "https://pxdata.stat.fi:443/PxWeb/api/v1/en/StatFin/icte/statfin_icte_pxt_13vg.px"

# with open('query2.json', 'r') as file:
#     json_query = json.load(file)

# response = requests.get(api_url, json=json_query)

# if response.status_code == 200:
#     data = response.json()

#     print(json.dumps(data, indent=4))
# else:
#     print("Failed to fetch data from API:", response.status_code)
#     print("Response content:", response.content)

api_url = "https://pxdata.stat.fi:443/PxWeb/api/v1/en/StatFin/icte/statfin_icte_pxt_13vg.px"

response = requests.get(api_url)

if not response.ok:
    print(f"Error: Can't download list from Tilastokeskus: {response.reason}")
    sys.exit(1)

data = response.json()
print(data)
