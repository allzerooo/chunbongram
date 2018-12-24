from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers

class Notifications(APIView):

    def get(self, request, format=None):

        user = request.user

        notifications = models.Notification.objects.filter(to=user)

        serializser = serializers.NotificationsSerializer(notifications, many=True)

        return Response(data=serializser.data, status=status.HTTP_200_OK)