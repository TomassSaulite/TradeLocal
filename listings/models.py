from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Listing(models.Model):
    title = models.CharField(max_length=200)               # short text
    description = models.TextField()                       # long text
    price = models.DecimalField(max_digits=10, decimal_places=2)  # number
    image = models.ImageField(upload_to='listingImages/')   # picture
    created_at = models.DateTimeField(auto_now_add=True)    # auto timestamp
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    phoneNum = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(max_length = 254,blank=True, null=True)
    def __str__(self):
        return self.title