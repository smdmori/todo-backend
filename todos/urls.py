from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import TodoDetail, TodoList, CategoryDetail, CategoryList, catTodos

urlpatterns = [
    path('', TodoList.as_view(), name='todo_list'),
    path('<int:pk>/', TodoDetail.as_view(), name='todo_detail'),
    path('cat/', CategoryList.as_view(), name='cat_list'),
    path('cat/<int:pk>/', CategoryDetail.as_view(), name='cat_list'),
    path('cat-todos/<int:pk>/', catTodos, name='cat_todos'),
]


# router = SimpleRouter()
# router.register('', TodoViewSet, basename='todos')
# router.register('cat', CategoryViewSet, basename='categories')
# 
# urlpatterns = router.urls
# 