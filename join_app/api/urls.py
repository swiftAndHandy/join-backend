from django.urls import path, include

from join_app.api.views import TaskViewSet, CategoryViewSet, ContactViewSet, SubtaskViewSet, SubtasksForTaskId, \
    SummaryView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet)
router.register('categories', CategoryViewSet)
router.register('contacts', ContactViewSet)
router.register('subtasks', SubtaskViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('tasks/<int:task_id>/subtasks/', SubtasksForTaskId.as_view()),
    path('summary/', SummaryView.as_view())
]