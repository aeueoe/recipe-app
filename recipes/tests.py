from django.test import TestCase
from .models import Recipe
from .forms import RecipesSearchForm

class RecipeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Recipe.objects.create(
            name='Tea', 
            cooking_time=5, 
            ingredients='tea-leaves, water, sugar',
            description='Add tea leaves to boiling water, then add sugar'
        )

    def test_description(self):
        recipe = Recipe.objects.get(id=1)
        name_max_length = recipe._meta.get_field('name').max_length
        self.assertEqual(name_max_length, 120)

    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        recipe_name_label = recipe._meta.get_field('name').verbose_name
        self.assertEqual(recipe_name_label, 'name')

    def test_cookingtime_helptext(self):
        recipe = Recipe.objects.get(id=1)
        recipe_cookingtime = recipe._meta.get_field('cooking_time').help_text
        self.assertEqual(recipe_cookingtime, 'In minutes')

    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), '/list/1/')

    def test_difficulty(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.difficulty, 'Easy')

   
    def test_max_length_name(self):
        recipe = Recipe(name='A' * 121, cooking_time=5, ingredients='test', description='test')
        with self.assertRaises(Exception):
            recipe.full_clean()  

class RecipesSearchFormTest(TestCase):

    def test_form_renders_recipe_diff_input(self):
        form = RecipesSearchForm()
        self.assertIn('recipe_diff', form.as_p())

    def test_form_renders_chart_type_input(self):
        form = RecipesSearchForm()
        self.assertIn('chart_type', form.as_p())

    def test_form_valid_data(self):
        form = RecipesSearchForm(data={'recipe_diff': '#1', 'chart_type': '#2'})
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = RecipesSearchForm(data={'recipe_diff': '', 'chart_type': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('This field is required.', form.errors['recipe_diff'])
        self.assertIn('This field is required.', form.errors['chart_type'])