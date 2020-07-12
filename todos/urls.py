from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import TodoViewSet, CategoryViewSet

router = SimpleRouter()
router.register('', TodoViewSet, basename='todos')
router.register('cat', CategoryViewSet, basename='categories')

urlpatterns = router.urls
