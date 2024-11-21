from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from .models import user
from .serializers import userSerializer
from .models import Client
from .serializers import ClientSerializer
from .models import Project
from .serializers import ProjectSerializer

class userViewSet(ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer