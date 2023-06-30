from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member,Whiskey
import pandas as pd

def displayImage(request):#defines the funtion display image and takes in requests as a parameter
  template = loader.get_template('display_image.html')#loads the template display_image.html when the displayImage function is called
  return HttpResponse(template.render({},request))#returns and render the template to the browser



def importFromCSV(request):
    dataframe = pd.read_csv('C:\\Users\\ELATT\\Desktop\\Python\\Paul-C-List-Manager\\Django\\my_tennis_club\\members\\data\\Whiskeyhunter.csv', encoding='latin1')  # Reads the CSV file 'Whiskeyhunter.csv' and stores the data in a Pandas DataFrame
    #dataframe = dataframe.tail(-1)

    for d in range(len(dataframe)): 
        drink = Whiskey()  # Creates an instance of the Whiskey class
        drink.dt = dataframe.iloc[d]['dt']
        drink.winning_bid_max = dataframe.iloc[d]['winning_bid_max']
        drink.winning_bid_min = dataframe.iloc[d]['winning_bid_min']
        drink.winning_bid_mean = dataframe.iloc[d]['winning_bid_mean']
        drink.auction_trading_volume = dataframe.iloc[d]['auction_trading_volume']
        drink.auction_lots_count = dataframe.iloc[d]['auction_lots_count']
        drink.all_auctions_lots_count = dataframe.iloc[d]['all_auctions_lots_count']
        drink.auction_name = dataframe.iloc[d]['auction_name']
        drink.auction_slug = dataframe.iloc[d]['auction_slug']
        #drink.save()

    return HttpResponse('Data imported successfully')

def whiskeydisplay(request):
    querySet = Whiskey.objects.all().values()
     # Retrieves all Whiskey objects from the database and returns a QuerySet of their values

    template = loader.get_template("whiskeybrowser.html")
    # Loads the template whiskeybrowser.html


    context = {
        "drink" : querySet
    }
    # Creates a context dictionary with the querySet as the value for the "drink" key

    return HttpResponse(template.render(context, request))
     # Returns and renders the template with the context to the browser











def filterByFirstname(request):
    queryset = Member.objects.filter(firstname=request.GET['firstname']).values()

    template = loader.get_template("details.html")
    context = {
        "mymember" : queryset[0]
    }
    return HttpResponse(template.render(context, request))
    



def firstnames(request):
    firstnames = Member.objects.values_list('firstname')
    template = loader.get_template('firstname.html')
    context = {
        "mymembers" : firstnames
    }
    return HttpResponse(template.render(context, request))


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers' : mymembers
    }
    return HttpResponse(template.render(context,request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        "mymember" : mymember
    }
    return HttpResponse(template.render(context, request))

def members2(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_memmbers2.html')
    context = {
        'mymembers' : mymembers
    }
    return HttpResponse(template.render(context,request))

def details2(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template("details2.html")
    context = {
        "mymember" : mymember
    }
    return HttpResponse(template.render(context, request))



def displaywhiskeydetails(request, id):
    mywhiskies = Whiskey.objects.get(id=id)
    template = loader.get_template("single_whiskey_details.html")
    context = {
        "drink" : mywhiskies
    }
    return HttpResponse(template.render(context, request))

def image(request):
    template=loader.get_template("Static.html")
    return HttpResponse(template.render({}, request))

















# Create your views here.
