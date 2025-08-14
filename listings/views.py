from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Listing



def allListings(request):
    if request.method=="POST":
        keyWord = request.POST['keyWord']
        listings1 = Listing.objects.filter(title__contains=keyWord)
        listings2 = Listing.objects.filter(description__contains=keyWord)
        listings = listings1.union(listings2) 

        return render(request, 'listings/allListings.html', {'listings': listings})

    else:
        listings = Listing.objects.all()
        return render(request, 'listings/allListings.html', {'listings': listings})




@login_required
def userListings(request):
    listings = Listing.objects.filter(owner=request.user)
    return render(request, 'listings/userListings.html', {'listings': listings})


@login_required
def createListing(request):
    if request.method=="POST":
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        image = request.FILES['image']
        owner = request.user
        Listing.objects.create(title=title,description=description, price=price,image=image,owner=owner)
        print("\033[93m"+f'New listing created: {title.title}'+"\033[0m")
        return redirect('listings:userListings') 
    return render(request, 'listings/createListing.html')
