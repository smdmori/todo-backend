from rest_framework import serializers
from .models import Todo, Category

class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('id', 'author', 'categories','title', 'body', 'done', 'updated_at', 'created_at', 'due_date',)

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'subject',)