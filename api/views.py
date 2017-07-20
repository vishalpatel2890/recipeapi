from api.models import Recipes, Ingredients, Steps
from rest_framework import viewsets
from api.serializers import RecipesSerializer, IngredientsSerializer, UserSerializer, StepsSerializer
from django.contrib.auth.models import User


class RecipesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows the Recipe List to be viewed or edited.
    """
    queryset = Recipes.objects.all().order_by('username')
    serializer_class = RecipesSerializer

class IngredientsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Ingredients to be viewed or edited.
    """
    queryset = Ingredients.objects.all().order_by('recipe')
    serializer_class = IngredientsSerializer

class IngredientsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Ingredients to be viewed or edited.
    """
    queryset = Steps.objects.all().order_by('recipe')
    serializer_class = StepsSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
