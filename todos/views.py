from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo, Category
from .serializers import TodoSerializer, CategorySerializer
from .permissions import IsAuthorOrReadOnly

class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@api_view(['get'])
def catTodos(request, pk):
    cat = Category.objects.get(pk=pk)
    cat.save()
    cat_todos = cat.todo_set.all()
    serializer = TodoSerializer(cat_todos,  many=True)
    return Response(serializer.data)
    # context_object_name = 'cat_todos'

    # def get_queryset(self):
        # return Category.objects.get(id=1).todo_set.all()
    

# class TodoViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthorOrReadOnly,)
    # queryset = Todo.objects.all()
    # serializer_class = TodoSerializer
# 
# class CategoryViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthorOrReadOnly,)    
    # queryset = Category.objects.all()
    # serializer_class = CategorySerializer
# 