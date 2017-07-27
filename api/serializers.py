from api.models import Recipes, Ingredients, Steps
from rest_framework import serializers
from django.contrib.auth.models import User


class RecipesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipes
        fields = ('id', 'recipename', 'yields', 'portionsize', 'username', 'dateadded', 'image', )
        # read_only_fields = ('image',)

class IngredientsSerializer(serializers.HyperlinkedModelSerializer):
    recipe = serializers.HyperlinkedRelatedField(many=False, view_name='recipe')
    
    class Meta:
        model = Ingredients
        fields = ('ingredient', 'quantity', 'measuresize', 'recipe', 'recipe_id')

class StepsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Steps
        fields = ('stepno', 'steps', 'recipe', 'recipe_id', 'step_image')


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)
