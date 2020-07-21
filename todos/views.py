from rest_framework import viewsets, generics, permissions, reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Todo, Category
from .serializers import TodoSerializer, CategorySerializer #, serialize_cat
from .permissions import IsAuthorOrReadOnly

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

# class TodoList(generics.ListCreateAPIView):
    # queryset = Todo.objects.all()
    # serializer_class = TodoSerializer
# 
# class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Todo.objects.all()
    # serializer_class = TodoSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# class CategoryList(generics.ListCreateAPIView):
    # queryset = Category.objects.all()
    # serializer_class = CategorySerializer
# 
# class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Category.objects.all()
    # serializer_class = CategorySerializer


@api_view(['get'])
def api_root(request, format=None):
    return ({
        'todos': reverse('todo-list', request=request, format=format),
        'categories': reverse('category-list', request=request, format=format),
    })

# @api_view(['get'])
# def catTodos(request, pk):
    # cat = Category.objects.get(pk=pk)
    # cat.save()
    # cat_todos = cat.todo_set.all()
    # serializer = TodoSerializer(cat_todos,  many=True)
    # serializer = serialize_todo(cat_todos)
    # return Response(serializer.data)
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