from rest_framework import serializers
from .models import Todo
# from categories.models import Category


# class CategorySerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Category
#         fields = ('subject',)

class TodoSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    class Meta:
        model = Todo
        fields = ('id', 'author', 'title', 'body', 'created_at',)