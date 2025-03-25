from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from join_app.api.serializers import TaskSerializer, CategorySerializer, ContactSerializer, ContactListSerializer, \
    SubtaskSerializer
from join_app.models import Task, Category, Contact, Subtask

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

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
        return Subtask.objects.filter(task_id=task_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('first_name', 'surname')

    def get_serializer_class(self):
        if self.action == 'list':
            return ContactListSerializer
        return ContactSerializer