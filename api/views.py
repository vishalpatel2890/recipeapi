from api.models import Recipes, Ingredients, Steps
from rest_framework import viewsets, filters, generics
from api.serializers import RecipesSerializer, IngredientsSerializer, UserSerializer, StepsSerializer
from django.contrib.auth.models import User

class RecipeNamesList(generics.ListAPIView):
    serializer_class = RecipesSerializer

    def get_queryset(self):
        queryset = Recipes.objects.all()
        workspace = self.request.query_params.get('recipename')
        queryset = queryset.filter(recipename=workspace)
        return queryset

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

class StepsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Ingredients to be viewed or edited.
    """
    queryset = Steps.objects.all().order_by('recipe')
    serializer_class = StepsSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
