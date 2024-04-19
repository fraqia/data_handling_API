import requests
import json

api_url = "https://pxdata.stat.fi/PXWeb/api/v1/en/StatFin/icte/statfin_icte_pxt_13vg.px"

with open('query.json', 'r') as file:
    json_query = json.load(file)