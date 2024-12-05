from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToDoItemViewSet, TagViewSet

router = DefaultRouter()
router.register(r'todos', ToDoItemViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
