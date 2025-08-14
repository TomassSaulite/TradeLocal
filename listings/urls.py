from django.urls import path
from . import views
app_name = 'listings'
urlpatterns = [
    path('userListings/', views.userListings, name='userListings'),
    path('createListing/', views.createListing, name='createListing'),
    path('allListings/', views.allListings, name='allListings'),

]
