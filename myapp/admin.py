from django.contrib import admin
from .models import *

# register models to Django admin
admin.site.register(Location)
admin.site.register(Park)
admin.site.register(Breed)
admin.site.register(Gender)
admin.site.register(Socialization)
admin.site.register(Aggression)
admin.site.register(Tag)
admin.site.register(Dog)
admin.site.register(User)
