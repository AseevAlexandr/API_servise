from django.shortcuts import render
from rest_framework import generics
from .models import Tasks
from .serializers import TasksSerializers


class TaskApiList(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializers


# class TaskApiUpdate(generics.UpdateAPIView):
#     queryset = Tasks.objects.all()
#     serializer_class = TasksSerializers


class TaskApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializers
