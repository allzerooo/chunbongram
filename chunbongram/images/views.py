from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

class Feed(APIView):

    def get(self, request, format=None):

        user = request.user

        following_users = user.following.all()

        image_list = []

        for following_user in following_users:
            
            # images 는 Image model 과 User 의 related_name
            user_images = following_user.images.all()[:2]

            for image in user_images:

                image_list.append(image)
        
        sorted_list = sorted(image_list, key=lambda image: image.created_at, reverse=True)

        serializer = serializers.ImageSerializer(sorted_list, many=True)

        return Response(serializer.data)


class LikeImage(APIView):

    def get(self, request, id, format=None):

        # url 을 요청한 현재 로그인 된 user
        user = request.user

        try:
            found_image = models.Image.objects.get(id=id)
        except models.Image.DoesNotExist:
            return Response(status=404)
        
        # models.py 의
        # def __str__(self):
        # return '{} - {}'.format(self.location, self.caption)
        # 에 해당하는 format 으로 출력됨
        # print(found_image)

        new_like = models.Like.objects.create(
            creator = user,
            image = found_image
        )

        new_like.save()

        return Response(status=200)