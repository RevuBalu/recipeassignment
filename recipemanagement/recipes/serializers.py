from django.contrib.auth.models import User
from rest_framework import serializers
from recipes.models import Recipe,Review
class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields=['Recipe_name','Recipe_ingredients','Recipe_instructions','cuisine','meal_type','created','updated']
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields =['recipename','user','rating','comment','date_added']

class UserSerializer(serializers.ModelSerializer):
        password = serializers.CharField(write_only=True)

        class Meta:
            model = User
            fields = ['id', 'username', 'password']

        def create(self, validated_data):  # after validation
            u = User.objects.create_user(username=validated_data['username'], password=validated_data['password'])
            u.save()
            return u