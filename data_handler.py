import requests
import json
from pprint import pprint

api_url = "https://api.tvmaze.com/singlesearch/shows"
params = {"q":"Star Wars Clone Wars"}

response = requests.get(api_url, params)

if response.status_code == 200:
    data = json.loads(response.text)
    # pprint(data)
    name = data['name']
    premiered = data['premiered']
    summary = data['summary']
    print(f"{name} premiered on {premiered}")
    print(summary)

else:
    print(f'Error: {response.status_code}')