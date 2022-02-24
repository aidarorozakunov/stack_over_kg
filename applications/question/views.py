from rest_framework import status, generics
from rest_framework.decorators import api_view
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from applications.question.models import Category
from applications.question.serializers import CategorySerializer

# 1 способ
# @api_viw(['GET'])
# def category_list(request):
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)

# 2 способ
# class CategoryView(APIView):
#     def get(self, request):
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# 3 способ
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


