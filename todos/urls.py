from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import TodoViewSet, CategoryViewSet
# checked #
router = SimpleRouter()
router.register('', TodoViewSet, basename='todos')
router.register('cat', CategoryViewSet, basename='categories')

urlpatterns = router.urls

# urlpatterns = [
    # path('<int:pk>/', TodoDetail.as_view()),
    # path('', TodoList.as_view()),
    # path('cat/<int:pk>/', CategoryDetail.as_view()),
    # path('cat/', CategoryList.as_view()),
# ]