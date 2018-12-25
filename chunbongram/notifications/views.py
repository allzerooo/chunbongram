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


# view 를 만들지 않고 function 을 사용하는 이유는 
# 다른 사람들이 내 알림 설정에 들어오는 공개적인 view 가 있을 수 없기 때문이다 
# view 에서 해당 function 을 불러오는 작업이 필요하다
def create_notification(creator, to, notification_type, image=None, comment=None):

    notification = models.Notification.objects.create(
        creator = creator,
        to = to,
        notification_type = notification_type,
        image = image,
        comment = comment
    )

    notification.save()