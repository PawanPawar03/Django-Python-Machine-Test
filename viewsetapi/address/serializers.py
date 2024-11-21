from rest_framework import serializers
from .models import user
from .models import Client
from .models import Project

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'Project_name','client_name', 'created_at', 'created_by']

