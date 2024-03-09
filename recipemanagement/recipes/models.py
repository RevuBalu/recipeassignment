from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Recipe(models.Model):
    Recipe_name=models.CharField(max_length=150)
    Recipe_ingredients=models.CharField(max_length=1000)
    Recipe_image = models.ImageField(upload_to='recipe', null=True, blank=True)
    cuisine = models.CharField(max_length=50,default='')
    meal_type = models.CharField(max_length=50,default='')
    Recipe_instructions=models.TextField(default='')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
         return self.Recipe_name
class Review(models.Model):
    recipename=models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1,validators=[MinValueValidator(0), MaxValueValidator(5)])
    comment=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.recipename.Recipe_name


