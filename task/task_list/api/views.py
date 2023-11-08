from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from django.http import HttpRequest
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response
from ..models import Task
from ..api.serializers import TaskSerializers


class TaskGenericApiView(GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = TaskSerializers
    queryset = Task.objects.all()

    def get(self, request: HttpRequest, *args: tuple, **kwargs: dict) -> Response:
        tasks = Task.objects.filter(user_id=self.request.user.id)
        serializer = TaskSerializers(tasks, many=True)
        return Response(serializer.data)

    def post(self, request: HttpRequest, *args: tuple, **kwargs: dict) -> Response:
        return self.create(request, *args, **kwargs)


class SingleTaskApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializers
    queryset = Task.objects.all()

    def retrieve(self, request: HttpRequest, *args: tuple, **kwargs: dict) -> Response:
        tasks = Task.objects.filter(user_id=self.request.user.id) & Task.objects.filter(
            id=kwargs["pk"]
        )
        serializer = TaskSerializers(tasks, many=True)
        return Response(serializer.data)
