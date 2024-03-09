from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

from recipes.models import Recipe

from recipes.serializers import RecipeSerializer

from recipes.serializers import UserSerializer

from recipes.models import Review

from recipes.serializers import ReviewSerializer
from rest_framework import viewsets


# Create your views here.
#list of all recipes and create a new recipe
class allrecipes(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self,request):
        r=Recipe.objects.all()
        rec=RecipeSerializer(r,many=True)
        return Response (rec.data,status=status.HTTP_200_OK)

    def post(self,request,format=None):
        r=RecipeSerializer(data=request.data)
        if r.is_valid():
            r.save()
            return Response(r.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
#retrive a particular recipe,edit a particular recipe and delete
class Recipedetail(APIView):
    permission_classes = [IsAuthenticated, ]
    def get_object(self,request,pk):
        try:

            return Recipe.objects.get(pk=pk)
        except:
            raise Http404

    def get(self,request,pk):
        recipe=self.get_object(request,pk)
        r= RecipeSerializer(recipe,many=True)
        return Response(r.data,status=status.HTTP_200_OK)
    def put(self, request, pk):
        recipe= self.get_object(request, pk)
        r = RecipeSerializer(recipe,data=request.data)
        if(r.is_valid()):
            r.save()
            return Response(r.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        recipe= self.get_object(request, pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#search of recipe by using title or ingredient or instruction
class search(APIView):
    def get(self,request):

        query=self.request.query_params.get('search')
        if (query):
            recipe=Recipe.objects.filter(Q(Recipe_name__icontains=query) | Q(Recipe_ingredients__icontains=query)| Q(Recipe_instructions__icontains=query))

            r=RecipeSerializer(recipe,many=True)
            return Response(r.data)
#search of recipe with common ingredients
class commoningredient(APIView):
    def get(self,request):

        query=self.request.query_params.get('commoningredient')
        if (query):
            recipe=Recipe.objects.filter(Recipe_ingredients__icontains=query)

            r=RecipeSerializer(recipe,many=True)
            return Response(r.data,status=status.HTTP_200_OK)
#search for recipe with common title
class commontitle(APIView):
    def get(self,request):

        query=self.request.query_params.get('commontitle')
        if (query):
            recipe=Recipe.objects.filter(Recipe_name__icontains=query)

            r=RecipeSerializer(recipe,many=True)
            return Response(r.data,status=status.HTTP_200_OK)
#filter by meal_type as snack,lunch and breakfast
class snack(viewsets.ModelViewSet):
    queryset=Recipe.objects.all()
    serializer_class=RecipeSerializer
    def get_queryset(self):
        qs=self.queryset
        queryset=qs.filter(meal_type="snack")
        return queryset

class lunch(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        qs = self.queryset
        queryset = qs.filter(meal_type="lunch")
        return queryset
class breakfast(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        qs = self.queryset
        queryset = qs.filter(meal_type="breakfast")
        return queryset
#filter by cuisine as indian or chineese
class indian(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        qs = self.queryset
        queryset = qs.filter(cuisine="indian")
        return queryset
class chineese(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        qs = self.queryset
        queryset = qs.filter(cuisine="chineese")
        return queryset
#get all users and create and login
class CreateUser(APIView):
    def get(self,request):
        u=User.objects.all()
        us=UserSerializer(u, many=True)
        return Response(us.data,status=status.HTTP_200_OK)

    def post(self,request):
        u=UserSerializer(data=request.data)
        if(u.is_valid()):
            u.save()
            return Response(u.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
#logout
class user_logout(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response (status=status.HTTP_200_OK)
#get all reviews and create new review
class allreview(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self,request):
        r=Review.objects.all()
        re=ReviewSerializer(r,many=True)
        return Response (re.data,status=status.HTTP_200_OK)


    def post(self,request,format=None):
        r=ReviewSerializer(data=request.data)
        if r.is_valid():
            r.save()
            return Response(r.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
#get particular review ,edit and delete
class Reviewdetail(APIView):
    permission_classes = [IsAuthenticated, ]
    def get_object(self,request,pk):
        try:

            return Review.objects.get(pk=pk)
        except:
            raise Http404

    def get(self,request,pk):
        review=self.get_object(request,pk)
        r= ReviewSerializer(review)
        return Response(r.data,status=status.HTTP_200_OK)


    def put(self, request, pk):
        review= self.get_object(request, pk)
        r = ReviewSerializer(review,data=request.data)
        if(r.is_valid()):
            r.save()
            return Response(r.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        review= self.get_object(request, pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
