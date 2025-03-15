from django.urls import path, include

from join_app.api.views import TaskViewSet, CategoryViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]