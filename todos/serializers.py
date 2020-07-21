from rest_framework import serializers
from .models import Todo, Category #, Order


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    subject = serializers.CharField()


class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    author = serializers.CharField()
    categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    title = serializers.CharField()
    body = serializers.CharField(style={'base_template': 'textarea.html'})
    done = serializers.BooleanField()
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    created_at = serializers.DateField(format="%Y-%m-%d %H:%M:%S")
    due_date = serializers.DateField(format="%Y-%m-%d %H:%M:%S")

# class OrderSerializer(serializers.Serializer):
    # category = serializers.CharField()
    # todo = serializers.CharField()
    # position = serializers.IntegerField()


# class TodoSerializer(serializers.ModelSerializer):
# 
    # class Meta:
        # model = Todo
        # fields = ('id', 'author', 'categories','title', 'body', 'done', 'updated_at', 'created_at', 'due_date',)




# class CategorySerializer(serializers.ModelSerializer):
# 
    # class Meta:
        # model = Category
        # fields = ('id', 'subject',)




# from typing import Dict, Any
#, validators
# from django.contrib.auth.models import User
#, CustomUser


# def serialize_cat(cat: Category) -> Dict[str, Any]:
    # return {
        # 'id': Category.id,
        # 'subject': Category.subject,
    # }

# def serialize_todo(todo: Todo) -> Dict[str, Any]:
    # return {
        # 'id': Todo.id,
        # 'author': Todo.author,
        # 'categories': Todo.categories,
        # 'title': Todo.title,
        # 'body': Todo.body,
        # 'done': Todo.done,
        # 'updated_at': Todo.updated_at.isoformat(),
        # 'created_at': Todo.created_at.isoformat(),
        # 'due_date': Todo.due_date.isoformat(),
    # }


# class TodoValidSerializer(serializers.ModelSerializer):
    # 
    # class Meta:
        # validators = [
            # validators.UniqueTogetherValidator(
                # queryset = Todo.objects.all(),
                # fields = ['list', 'position'],
            # )
        # ]




# class UserSerializer(serializers.ModelSerializer):
    # 
    # user_name = serializers.CharField(source='username')
# 
    # class Meta:
        # model = CustomUser
        # fields = ('id', 'user_name', 'email', 'first_name', 'last_name',)