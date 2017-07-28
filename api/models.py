from django.db import models
from django.contrib.auth.models import User


class Recipes(models.Model):
    id = models.AutoField(primary_key=True)
    recipename = models.CharField(max_length=50, default='Enter A Recipe Name')
    yields = models.IntegerField(default='1')
    portionsize = models.CharField(max_length=50, default='Enter Portion Size')
    username = models.ForeignKey(User, default='https://quiet-citadel-22666.herokuapp.com/user/1/')
    dateadded = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='recipes', default='static/about-black-1240x600.jpg', height_field=None, width_field=None, max_length=100)



    def __str__(self):
        # return self.id
        return self.recipename
        return self.yields
        return self.portionsizes
        return self.image

class Ingredients(models.Model):
    ingredient = models.CharField(max_length=50, default='flour')
    quantity = models.FloatField(default='100')
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

    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, default='1')

    def __str__(self):
        return self.ingredient
        return self.quantity
        return self.measuresize
        return self.recipe

class Steps(models.Model):
    id = models.AutoField(primary_key=True)
    stepno = models.IntegerField()
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    steps = models.TextField()
    step_image = models.ImageField(upload_to="", default='static/about-black-1240x600.jpg', height_field=None, width_field=None, max_length=100)

    class Meta:
        unique_together = ('recipe', 'stepno',)

    def __str__(self):
        return self.id
        return self.stepno
        return self.steps
        return self.recipe
        return self.step_image
