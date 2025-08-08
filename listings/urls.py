from django.urls import path
from . import views

urlpatterns = [
    path('userListings/', views.userListings, name='userListings'),
    path('createListing/', views.createListing, name='createListing'),
]
