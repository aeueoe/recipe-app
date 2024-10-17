from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, logout_view, about


app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('list/', RecipeListView.as_view(), name='list'),
    path('list/<int:pk>/', RecipeDetailView.as_view(), name='details'),
    path('logout/', logout_view, name='logout'),
    path('about/', about, name='about'),
     
]