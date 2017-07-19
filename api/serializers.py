from api.models import Recipes, Ingredients
from rest_framework import serializers
from django.contrib.auth.models import User


class RecipesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipes
        fields = ('id', 'recipename', 'yields', 'portionsize', 'username', 'dateadded')

class IngredientsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredients
        fields = ('ingredient', 'quantity', 'measuresize', 'recipe')

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)
