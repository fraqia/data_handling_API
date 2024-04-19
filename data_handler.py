import requests
import json
import sys
from pprint import pprint

api_url = "https://pxdata.stat.fi/PxWeb/api/v1/en/StatFin/icte/statfin_icte_pxt_13vg.px"

response = requests.get(api_url)

if not response.ok:
    print(f"Error: Can't download list from Tilastokeskus: {response.reason}")
    sys.exit(1)

data = response.json()
pprint(data)

# for header in data:
#     print(header)

# print(data['title'])
# print(data['variables'])

# for variable in data['variables']:
#     pprint(variable)


