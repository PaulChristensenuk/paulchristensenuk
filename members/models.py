from django.db import models

# Create your models here.

class Member(models.Model):#create a class called Member taking in Model as parameter
    firstname = models.CharField(max_length=255)#defining a class called member passing as a parameter an instance model
    lastname = models.CharField(max_length=255)#using the models assign and set the field datatype and size to Char(acter)
    phone = models.BigIntegerField(null=True)#using the models assign and set the field datatype and size to Char(acter)
    joined_date = models.DateField(null=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    
class Whiskey(models.Model):#create a class called Whiskeys taking in Model as parameter
    dt = models.DateField(null=True)#dt field is defined using the field type date field
    winning_bid_max = models.FloatField()#winning_bid_max field is defined using the field type Floatfield
    winning_bid_min = models.FloatField()#winning_bid_min field is defined using the field type Floatfield
    winning_bid_mean = models.FloatField()#winning_bid_mean field is defined using the field type Floatfield
    auction_trading_volume = models.FloatField()# auction_trading_volume field is defined using the field type Floatfield
    auction_lots_count = models.IntegerField()#auction_lots_count field is defined using the field type Integerfield
    all_auctions_lots_count = models.IntegerField()#all_auctions_lots_count field is defined using the field type Integerfield
    auction_name = models.CharField(max_length=200)#auction_name field is defined using the field type Charfield
    auction_slug = models.SlugField(max_length=200)#auction_Slug is defined using the field type Slugfield

    def __str__(self):#converts the instance of the class to a string
        return self.auction_name





    
    