from django.db import models
from django.contrib.auth.models import User

# class Recipes(models.Model):
#     id = models.AutoField(primary_key=True)
#     recipename = models.CharField(max_length=50)
#     yields = models.IntegerField()
#     portionsize = models.CharField(max_length=50)
#     username = models.ForeignKey(User)
#     dateadded = models.DateField(auto_now_add=True)
#
#
#
#     def __unicode__(self):
#         return self.id
#         return self.recipename
#         return self.yields
#         return self.portionsizes

class Recipes(models.Model):
    id = models.AutoField(primary_key=True)
    recipename = models.CharField(max_length=50)
    yields = models.IntegerField()
    portionsize = models.CharField(max_length=50)
    username = models.ForeignKey(User)
    dateadded = models.DateField(auto_now_add=True)



    def __str__(self):
        # return self.id
        return self.recipename
        return self.yields
        return self.portionsizes

class Ingredients(models.Model):
    ingredient = models.CharField(max_length=50)
    quantity = models.FloatField()
    MEASURE_SIZES = (
        ('PNCH', 'PINCH'),
        ('TSP', 'TSP'),
        ('TBSP', 'TBSP'),
        ('CUP', 'CUP'),
        ('PINT', 'PINT'),
        ('QT', 'QUART'),
        ('GAL', 'GALLON'),
        ('G', 'GRAM'),
        ('KG', 'KILOGRAM'),
        ('OZ', 'OUNCE'),
        ('FLOZ', 'FLUID OUNCE'),
            )

    measuresize = models.CharField(
        max_length=4,
        choices=MEASURE_SIZES,
        default = 'TBSP'
        )

    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredient
        return self.quantity
        return self.measuresize
        return self.recipe
