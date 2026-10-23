
from tasks.models import Task
from tasks.serializers import Taskserializers
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView


class TaskCreateAPIView(ListCreateAPIView):
    queryset=Task.objects.all()
    serializer_class=Taskserializers

class TaskDetailsAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Task.objects.all()
    serializer_class=Taskserializers