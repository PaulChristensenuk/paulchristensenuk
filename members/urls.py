from django.urls import path
from . import views

#List of URL patterns for members App

urlpatterns =[
    
    path('members/', views.members, name='members'),#Map the URL 'members' to the members view with the name 'members'
    path('members/details/<int:id>', views.details, name='details'),#Map the URL 'members' to the members/details/<int:id>  with the name 'details
    path('members2/', views.members2, name='members2'),#Map the URL 'members2' to the members2 view with the name 'members2'
    path('members2/details2/<int:id>', views.details2, name='details2'), # Map the URL 'members2/details2/<int:id>' to the details2 view with the name 'details2'
    path('members/search-member', views.filterByFirstname, name='searchMember'),# Map the URL 'members/search-member' to the filterByFirstname view with the name 'searchMember'
    path('members/dislplay-image', views.image, name='displayImage'), # Map the URL 'members/display-image' to the image view with the name 'displayImage'
    path('members/import-data', views.importFromCSV, name='importData'), # Map the URL 'members/import-data' to the importFromCSV view with the name 'importData'
    path('members/whiskeyhunter', views.whiskeydisplay, name='whiskeyhunter'),# Map the URL 'members/whiskeyhunter' to the whiskeydisplay view with the name 'whiskeyhunter'
    path('members/displayimage', views.displayImage, name='displayimage'), # Map the URL 'members/displayimage' to the displayImage view with the name 'displayimage'
    path('members/detailswhiskey/<int:id>', views.displaywhiskeydetails, name='displaywhiskeydetails'), # Map the URL 'members/detailswhiskey/<int:id>' to the displaywhiskeydetails view with the name 'displaywhiskeydetails'
    ]