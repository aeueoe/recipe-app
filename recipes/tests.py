from django.test import TestCase
from .models import Recipe

class RecipeModelTestCase(TestCase):
    def test_recipe_name_max_length(self):
        recipe = Recipe(name='A' * 255, cooking_time='30 minutes', ingredients='Test ingredients', description='Test description')
        recipe.full_clean()

    def test_recipe_cooking_time_max_length(self):
        recipe = Recipe(name='Test recipe', cooking_time='A' * 50, ingredients='Test ingredients', description='Test description')
        recipe.full_clean()

    def test_recipe_ingredients_text_field(self):
        recipe = Recipe(name='Test recipe', cooking_time='30 minutes', ingredients='This is a test recipe', description='Test description')
        self.assertEqual(recipe.ingredients, 'This is a test recipe')

    def test_recipe_description_text_field(self):
        recipe = Recipe(name='Test recipe', cooking_time='30 minutes', ingredients='Test ingredients', description='This is a test recipe description')
        self.assertEqual(recipe.description, 'This is a test recipe description')