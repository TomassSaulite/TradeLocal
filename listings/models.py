from django.db import models
from django.contrib.auth.models import User

class Listing(models.Model):
    title = models.CharField(max_length=200)               # short text
    description = models.TextField()                       # long text
    price = models.DecimalField(max_digits=10, decimal_places=2)  # number
    image = models.ImageField(upload_to='listingImages/')   # picture
    created_at = models.DateTimeField(auto_now_add=True)    # auto timestamp
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title