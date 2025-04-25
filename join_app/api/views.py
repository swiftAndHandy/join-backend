from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from join_app.api.serializers import TaskSerializer, CategorySerializer, ContactSerializer, ContactListSerializer, \
    SubtaskSerializer, SummarySerializer
from join_app.models import Task, Category, Contact, Subtask

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class SummaryView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = SummarySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubtaskViewSet(viewsets.ModelViewSet):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer

class SubtasksForTaskId(ListAPIView):
    serializer_class = SubtaskSerializer

    def get_queryset(self):
        task_id = self.kwargs['task_id']
        get_object_or_404(Task, id=task_id)
        return Subtask.objects.filter(task_id=task_id)

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('first_name', 'surname')

    def get_serializer_class(self):
        if self.action == 'list':
            return ContactListSerializer
        return ContactSerializer