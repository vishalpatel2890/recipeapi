from django.contrib import admin
from api.models import Recipes,Ingredients, Steps

admin.site.register(Recipes)
admin.site.register(Ingredients)
admin.site.register(Steps)
