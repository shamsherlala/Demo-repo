import requests
import pandas as pd

payload = {'api_key': 'd928d0b82e0b19ff9a6169e48522bca4', 'query': 'drone', 'num': '20'}
response = requests.get('https://api.scraperapi.com/structured/twitter/search', params=payload)
data = response.json()

