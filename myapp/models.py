from django.db import models

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