from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self):
        return self.food
        

# Create your models here.
class Recipe(models.Model):
    ingredient = models.ManyToManyField(Ingredient,blank=True)
    name = models.CharField(max_length=50)
    desc = models.TextField()
    instruction = models.TextField()

    def __str__(self):
        return self.name
    