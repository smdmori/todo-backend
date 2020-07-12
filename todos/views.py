from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .models import Todo, Category
from .serializers import TodoSerializer, CategorySerializer
from .permissions import IsAuthorOrReadOnly

class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# class CategoryDetail(generics.RetrieveAPIView):
    # queryset = Category.objects.all()
    # serializer_class = CategorySerializer

# class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Todo.objects.all()
    # serializer_class = TodoSerializer