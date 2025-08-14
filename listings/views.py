from django.contrib.auth import authenticate, login
from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Listing
import os
from django.conf import settings

@login_required
def editListing(request, id):
    listing = get_object_or_404(Listing, id=id, owner=request.user)

    if request.method == 'POST':
        listing.title = request.POST.get('title', listing.title)
        listing.description = request.POST.get('description', listing.description)
        listing.phoneNum = request.POST.get('phoneNum', listing.phoneNum)
        listing.email = request.POST.get('email', listing.email)
        
        price = request.POST.get('price')
        if price:
            try:
                listing.price = float(price)
            except ValueError:
               
                return render(request, 'listings/editListing.html', {
                    'listing': listing,
                    'error': 'Invalid price value.'
                })

        if request.FILES.get('image'):
            listing.image = request.FILES['image']

        listing.save()
        return redirect('listings:userListings')

    return render(request, 'listings/editListing.html', {'listing': listing})

@login_required
def removeListing(request, id):
    listing = get_object_or_404(Listing, id=id, owner=request.user)
    if request.method == "POST":

        if listing.image:
            image_path = listing.image.path
            if os.path.isfile(image_path):
                os.remove(image_path)
        listing.delete()
        return redirect('listings:userListings')
    return redirect('listings:userListings')


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
        phoneNum = request.POST['phoneNum']
        email = request.POST['email']
        owner = request.user
        Listing.objects.create(title=title,description=description, price=price,image=image,phoneNum=phoneNum,email=email,owner=owner)
        print("\033[93m"+f'New listing created: {title.title}'+"\033[0m")
        return redirect('listings:userListings') 
    return render(request, 'listings/createListing.html')
