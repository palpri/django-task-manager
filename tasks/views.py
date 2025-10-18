from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer


class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer


# Allow list to be read by anyone; creation requires authentication
    def get_permissions(self):
       if self.request.method == 'POST':
          return [permissions.IsAuthenticated()]
       return [permissions.AllowAny()]


class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]