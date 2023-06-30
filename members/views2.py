from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member,Whiskey
import pandas as pd

def updateName(request, pk):
    Member = get_object_or_404(Member, pk=pk)

    if request.method - 'post':
        form = NameForm(request.POST)

        if form.is_valid():
            member.firstname = form.cleaned_data['name']
            member.save()

            return.HttpResponseRedirect(reverse('nameUdateSuccess'))
    else:
        form = NameForm()

        context = {
            form: form
        }
        template = loader.get_template('test.html')

        return HttpResponse(template.render(context, request))

def importFromCSV(request):
    dataframe = pd.read_csv('/Users/node666/Sites/django-tutorial/my_tennis_club/members/data/drinks2.csv', encoding='latin1')
    dataframe = dataframe.tail(-1)

    for d in range(len(dataframe)): 
        drink = Whiskey()
        drink.winning_bid_max = dataframe.iloc[d]['winning_bid_max']
        drink.winning_bid_min = dataframe.iloc[d]['winning_bid_min']
        drink.winning_bid_mean = pd.to_datetime(dataframe.iloc[d]['winning_bid_mean'])
        drink.auction_trading_volume = dataframe.iloc[d]['auction_trading_volume']
        drink.auction_lots_count = dataframe.iloc[d]['auction_lots_count']
        drink.all_auctions_lots_count = dataframe.iloc[d]['all_auction_lots_count']
        drink.auction_name = float(dataframe.iloc[d]['auction_name'].split(' ')[0])
        drink.auction_slug = dataframe.iloc[d]['auction_slug']
        drink.save()

    return HttpResponse('Data imported successfully')














def filterByFirstname(request):
    queryset = Member.objects.filter(firstname=request.GET['name']).values()

    template = loader.get_template("details.html")
    context = {
        "mymember" : queryset
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
    template = loader.get_template('first.html')
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

def whiskies(request):
    mywhiskies = Member.objects.all().values()
    template = loader.get_template('all_whiskies.html')
    context = {
        'mywhiskies' : mywhiskies
    }
    return HttpResponse(template.render(context,request))

def all_whiskies_details(request, id):
    mywhisky = Member.objects.get(id=id)
    template = loader.get_template("all_whiskies_details.html")
    context = {
        "mywhisky" : mywhisky
    }
    return HttpResponse(template.render(context, request))

def image(request):
    template=loader.get_template("Static.html")
    return HttpResponse(template.render({},request))

















# Create your views here.
