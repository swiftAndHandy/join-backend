from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from join_app.api.serializers import TaskSerializer, CategorySerializer, ContactSerializer
from join_app.models import Task, Category, Contact


@api_view()
def hello_world(request):
    return Response({'hello': 'world'})


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer