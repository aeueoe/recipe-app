from django.db import models
from django.shortcuts import reverse

class Recipe(models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.FloatField(help_text='In minutes')
    ingredients = models.CharField(max_length=350)
    description = models.TextField()
    pic = models.ImageField(upload_to='recipes', default='no_image.jpg')

    @property
    def difficulty(self):
        ingredients = self.ingredients.split(', ')
        cooking_time_minutes = float(self.cooking_time)
        if cooking_time_minutes < 30 and len(ingredients) < 7:
            return 'Easy'
        elif cooking_time_minutes < 30 and len(ingredients) >= 7:
            return 'Medium'
        elif cooking_time_minutes >= 30 and len(ingredients) < 7:
            return 'Intermediate'
        elif cooking_time_minutes >= 30 and len(ingredients) >= 7:
            return 'Hard'

    def get_absolute_url(self):
        return reverse('recipes:details', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.name)