#Import the necessary modules to work with the CSV file
import csv


#Define the name class called myclass
class myclass:
    #contructor to initialize the class that was created.
    def __init__(self,whiskies):
        self.dt = whiskies[0]#Assign the first item in the list (dt) date attribute
        self.winning_bid_max = whiskies[1]#Assign the first item in the list winning_bid_max attribute
        self.winning_bid_min = whiskies[2]#Assign the first item in the list winning_bid_min attribute
        self.winning_bid_mean = whiskies[3]#Assign the first item in the list winning_bid_mean attribute
        self.auction_trading_volume = whiskies[4]#Assign the first item in the list auction_trading_volume attribute
        self.auction_lots_count = whiskies[5]#Assign the first item in the list auction_lots_count attribute
        self.all_auctions_lots_count = whiskies[6]#Assign the first item in the list all_auctions_lots_count attribute
        self.auction_name = whiskies[7]#Assign the first item in the list auction_name attribute
        self.auction_slug = whiskies[8] #Assign the first item in the list auction_slug attribute

#List of headers for the CSV file                
headers = ['dt', 'winning_bid_max', 'winning_bid_min', 'winning_bid_mean', 'auction_trading_volume', 'auction_lots_count','all_auctions_lots_count', 'auction_name', 'auction_slug']

#Create an empty list called whiskey file to store the myclass list     
whiskeyfile = []
with open ("Whiskeyhunter.csv","r") as fred:#Open the CSV file in read mode, create a CSV reader object to read the file
    whiskeydata = csv.reader(fred)
    for items in whiskeydata:#Iterate over each row in the CSV file and create a new instance for myclass and append to whiskey file
        whiskeyfile.append(myclass(items))
xx = input("Please enter winning bid max")#Get input from user and assign it to xx
for items in whiskeyfile:#Iterate over each row in the whiskey file
    if xx==items.winning_bid_max:#If user input equals winning bid exicute the statement below
        print(items.dt, items.winning_bid_max,items.auction_name,items.auction_trading_volume)


        
        
                
        
        
        

