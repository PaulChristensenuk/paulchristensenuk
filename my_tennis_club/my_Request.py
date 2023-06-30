import requests #allows you to send http requests using python
import json
import os
import csv

file_path=os.path.dirname(os.path.abspath(__file__))
api_get=requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=gbp&order=market_cap_desc&per_page=100&page=1&sparkline=false')
api=json.loads(api_get.content)

with open (f'{file_path}/test.csv',"w",newline='') as test:
    csv_file=csv.DictWriter(test,fieldnames=list(api[0].keys()))
    csv_file.writeheader()
    csv_file.writerows(api)
