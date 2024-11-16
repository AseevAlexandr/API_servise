from django.shortcuts import render
from rest_framework import generics
from .models import Tasks
from .serializers import TasksSerializers
from rest_framework import viewsets


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializers
