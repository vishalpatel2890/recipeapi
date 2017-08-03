from api.models import Recipes, Ingredients, Steps
from rest_framework import serializers
from django.contrib.auth.models import User


class RecipesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipes
        fields = ('id', 'recipename', 'yields', 'portionsize', 'username', 'dateadded', 'image', )

class IngredientsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredients
        fields = ('id', 'ingredient', 'quantity', 'measuresize', 'recipe', 'recipe_id')

class StepsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Steps
        fields = ('id', 'stepno', 'steps', 'recipe', 'recipe_id', 'step_image')


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)
