from rest_framework import serializers
from .models import Task, CustomUser


class TaskSerializers(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ["id", "user", "title", "description", "created_at", "completed"]
