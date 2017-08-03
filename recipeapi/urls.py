from django.conf.urls import url, include
from rest_framework import routers
from api import views
from api.views import RecipeNamesList, IngredientsList, StepsList, IngredientsViewSet, ingredients

router = routers.DefaultRouter()
router.register(r'recipes', views.RecipesViewSet)
# router.register(r'ingredients', views.IngredientsViewSet)
router.register(r'steps', views.StepsViewSet)
router.register(r'user', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^recipesearch/(?P<recipename>.+)/$', RecipeNamesList.as_view()),
    url(r'^ingredientsearch/(?P<recipeid>.+)/$', IngredientsList.as_view()),
    url(r'^stepsearch/(?P<recipeid>.+)/$', StepsList.as_view()),
    url(r'^ingredients/$', ingredients, name='ingredients'),

]
