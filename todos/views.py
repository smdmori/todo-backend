from rest_framework import viewsets
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
