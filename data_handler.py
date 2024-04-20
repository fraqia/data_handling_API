import requests
import json
from pprint import pprint

api_url = "https://api.tvmaze.com/singlesearch/shows"
params = {"q":"Girls"}

response = requests.get(api_url, params)

if response.status_code == 200:
    data = json.loads(response.text)
    pprint(data)

else:
    print(f'Error: {response.status_code}')