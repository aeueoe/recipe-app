from django.db import models

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    cooking_time = models.CharField(max_length=50)
    ingredients = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name