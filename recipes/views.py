from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Recipe

def home(request):
    return render(request, 'recipes/recipes_home.html')

class RecipeListView(ListView):                       
    model = Recipe                                                        
    template_name = 'recipes/main.html'      
                    
class RecipeDetailView(DetailView):                  
    model = Recipe                                                        
    template_name = 'recipes/details.html'

def logout_view(request):
    logout(request)
    return redirect('recipes:home')