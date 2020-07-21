from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import TodoDetail, TodoList, CategoryDetail, CategoryList, catTodos
from todos import views

# urlpatterns = [
    # path('', TodoList.as_view(), name='todo-list'),
    # path('<int:pk>/', TodoDetail.as_view(), name='todo-detail'),
    # path('cat/', CategoryList.as_view(), name='categpry-list'),
    # path('cat/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    # path('cat-todos/<int:pk>/', catTodos, name='category-todos'),
# ]

router = DefaultRouter()
router.register(r'todos', views.TodoViewSet, basename='todos')
router.register(r'cats', views.CategoryViewSet, basename='categories')
# router.register(r'cat-todos/', views.catTodos, 'category-todos-list')

urlpatterns = [
    path('' ,include(router.urls)),
]

