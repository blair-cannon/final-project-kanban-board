from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Referecned model classes:

class Location(models.Model):
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=5)

    def __str__(self):
        return self.city
    
class Park(models.Model):
    name = models.CharField(max_length=500)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Breed(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Gender(models.Model):
    label = models.CharField(max_length=150)

    def __str__(self):
        return self.label

class Socialization(models.Model):
    label = models.CharField(max_length=500)

    def __str__(self):
        return self.label

class Aggression(models.Model):
    label = models.CharField(max_length=500)

    def __str__(self):
        return self.label

class Tag(models.Model):
    label = models.CharField(max_length=500)

    def __str__(self):
        return self.label

class Size(models.Model):
    label = models.CharField(max_length=500)

    def __str__(self):
        return self.label

# Models with foriegn keys

# Extending User model
class User(AbstractUser):
    second_parent = models.CharField(max_length=300, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)

class Dog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    age = models.CharField(max_length=300)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    birthday = models.DateField(blank=True, null=True)
    about_me = models.CharField(max_length=2000, blank=True, null=True)
    favorite_park = models.ForeignKey(Park, on_delete=models.CASCADE, blank=True, null=True)
    socialization = models.ForeignKey(Socialization, on_delete=models.CASCADE)
    aggression = models.ForeignKey(Aggression, on_delete=models.CASCADE)
    is_fixed = models.BooleanField()
    has_bitten = models.BooleanField()
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name









