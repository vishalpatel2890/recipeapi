from api.models import Recipes, Ingredients, Steps
from rest_framework import viewsets, filters, generics, mixins
from api.serializers import RecipesSerializer, IngredientsSerializer, UserSerializer, StepsSerializer
from django.contrib.auth.models import User
from rest_framework.parsers import MultiPartParser, FormParser

class RecipesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows the Recipe List to be viewed or edited.
    """
    queryset = Recipes.objects.all().order_by('username')
    serializer_class = RecipesSerializer
    parser_classes = (MultiPartParser, FormParser)

class IngredientsViewSet(viewsets.GenericAPIView):
    """
    API endpoint that allows Ingredients to be viewed or edited.
    """
    queryset = Ingredients.objects.all().order_by('recipe')
    serializer_class = IngredientsSerializer


class StepsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Ingredients to be viewed or edited.
    """
    queryset = Steps.objects.all().order_by('recipe')
    serializer_class = StepsSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RecipeNamesList(generics.ListAPIView):
    serializer_class = RecipesSerializer

    def get_queryset(self):
        queryset = Recipes.objects.all()
        recipe = self.request.query_params.get('recipename')
        queryset = queryset.filter(recipename=recipe)
        return queryset

class IngredientsList(generics.ListAPIView):
    serializer_class = IngredientsSerializer

    def get_queryset(self):
        queryset = Ingredients.objects.all()
        recipeid = self.request.query_params.get('recipeid')
        queryset = queryset.filter(recipe_id=recipeid)
        return queryset

class StepsList(generics.ListAPIView):
    serializer_class = StepsSerializer

    def get_queryset(self):
        queryset = Steps.objects.all()
        recipeid = self.request.query_params.get('recipeid')
        queryset = queryset.filter(recipe_id=recipeid)
        return queryset
