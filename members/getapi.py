import requests #allows you to send http my requests using python
import json
import csv

api_get=requests.get('https://whiskyhunter.net/api/auctions_data/?format=json')

#x = json.loads(api_get.content)
#y = api_get.json()


whiskies=['dt' , 'winning_bid_max', 'winning_bid_min', 'winning_bid_mean', 'auction_trading_volume', 'auction_lots_count', 'all_auctions_lots_count', 'auction_name', 'auction_slug']

with open ('Whiskeyhunter.csv','w',newline='') as fileW:
    whisky_file=csv.DictWriter(fileW,headers)
    whisky_file.writeheader()
    my_whisky = api_get.json()
    for whiskies in my_whisky:
        whisky_file.writerow(whiskies)