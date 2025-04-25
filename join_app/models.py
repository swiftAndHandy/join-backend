from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=5)
    city = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    badge_color = models.CharField(max_length=9)

class Category(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=30)

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    end_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    priority = models.IntegerField()
    state = models.IntegerField()

    assigned_users = models.ManyToManyField(User, related_name='tasks', blank=True)
    assigned_contacts = models.ManyToManyField(Contact, related_name='tasks', blank=True)

class Subtask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)