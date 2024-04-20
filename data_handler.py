import requests
import json

api_url = "https://api.tvmaze.com/singlesearch/shows"
params = {"q":"Girls"}

response = requests.get(api_url, params)

if response.status_code == 200:
    print(response.text)
else:
    print(f'Error: {response.status_code}')