from django.db import models
from django.contrib.auth.models import User

# Create your models here.

VEHICLE_TYPES = (
    ('Sedan', 'Sedan'), 
    ('Coupe', 'Coupe'), 
    ('Sports Car', 'Sports Car'),
    ('Station Wagon', 'Station Wagon'),
    ('Hatchback', 'Hatchback'), 
    ('Convertible', 'Convertible'), 
    ('SUV', 'SUV'), 
    ('Minivan', 'Minivan'), 
    ('Truck', 'Truck') 
)

RATING = (
    ('1', '1'), 
    ('2', '2'), 
    ('3', '3'), 
    ('4', '4'), 
    ('5', '5')
)

class Rating(models.Model): 
    reviewee = models.ForeignKey(User, related_name='user_reviewee', on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.PROTECT)
    comment = models.CharField(max_length=250, blank=True)
    rating = models.CharField(max_length=1, choices = RATING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pk

    class Meta: 
        ordering = ['created_at']

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image_link = models.CharField(max_length=250, blank=True)
    phone_number = models.CharField(max_length=11)
    zip_code = models.CharField(max_length=5)
    vehicle_type = models.CharField(max_length=15, blank=True, choices = VEHICLE_TYPES)
    vehicle_make = models.CharField(blank=True, max_length=15)
    vehicle_model = models.CharField(max_length=15, blank=True)
    num_seats = models.IntegerField(blank=True, null=True)
    fee = models.CharField(max_length=160, blank=True)
    available = models.BooleanField
    bio = models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    contacts = models.ManyToManyField(User, related_name = "profile_contacts", blank=True)
    ratings = models.ManyToManyField(Rating, blank=True)

    def __str__(self):
        return self.name

    class Meta: 
        ordering = ['name']

