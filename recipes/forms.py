from django import forms
from .models import Recipe

# Choices for chart type and difficulty level
CHART_CHOICES = (
    ('#1', 'Bar Chart'),
    ('#2', 'Pie Chart'),
    ('#3', 'Line Chart'),
)

DIFFICULTY_CHOICES = (
    ('#1', 'Easy'),
    ('#2', 'Medium'),
    ('#3', 'Intermediate'),
    ('#4', 'Hard'),
)


class RecipesSearchForm(forms.Form):
    recipe_diff = forms.ChoiceField(choices=DIFFICULTY_CHOICES)
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'cooking_time', 'ingredients', 'description', 'pic']