from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import RecipesSearchForm
import pandas as pd
from .utils import get_chart
from django.db.models import Count, Case, Value, When, CharField
from .forms import RecipesSearchForm, RecipeForm 

def home(request):
    return render(request, 'recipes/recipes_home.html')

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/main.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/details.html'

@login_required
def records(request):
    form = RecipesSearchForm(request.POST or None)
    recipe_df = None
    chart = None
    qs = None
    
    if request.method == 'POST' and form.is_valid():
        recipe_diff = form.cleaned_data['recipe_diff']
        chart_type = form.cleaned_data['chart_type']
        
        difficulty_map = {
            '#1': 'Easy',
            '#2': 'Medium',
            '#3': 'Intermediate',
            '#4': 'Hard'
        }
        recipe_diff = difficulty_map.get(recipe_diff)

        if recipe_diff:
            qs = Recipe.objects.annotate(
                ingredient_count=Count('ingredients'),
                calculated_difficulty=Case(
                    When(cooking_time__lt=20, ingredient_count__lt=6, then=Value('Easy')),
                    When(cooking_time__lt=20, ingredient_count__gte=6, then=Value('Medium')),
                    When(cooking_time__gte=20, ingredient_count__lt=6, then=Value('Intermediate')),
                    When(cooking_time__gte=20, ingredient_count__gte=6, then=Value('Hard')),
                    default=Value('Unknown'),
                    output_field=CharField()
                )
            ).filter(calculated_difficulty=recipe_diff)

            if qs.exists():
                
                data = []
                for recipe in qs:
                    data.append({
                        'name': recipe.name,  
                        'cooking_time': recipe.cooking_time,
                        'difficulty': recipe.calculated_difficulty  
                    })
                recipe_df = pd.DataFrame(data)
                chart = get_chart(chart_type, recipe_df, labels=recipe_df['name'].values)
                recipe_df = recipe_df.to_html(escape=False)

    context = {
        'form': form,
        'recipes': qs,  
        'chart': chart,
    }
    return render(request, 'recipes/search.html', context)



def logout_view(request):
    logout(request)
    return redirect('recipes:home')

def about(request):
    return render(request, 'recipes/about.html')

@login_required
def add_recipe_view(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipes:list')  
    else:
        form = RecipeForm()

    return render(request, 'recipes/add_recipe.html', {'form': form})