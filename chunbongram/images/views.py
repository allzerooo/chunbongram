from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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

        # 해당 id 를 갖는 image 를 탐색
        try:
            found_image = models.Image.objects.get(id=id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        # models.py 의
        # def __str__(self):
        # return '{} - {}'.format(self.location, self.caption)
        # 에 해당하는 format 으로 출력됨
        # print(found_image)

        try:
            # 해당 좋아요가 존재하는지 탐색
            preexisting_like = models.Like.objects.get(
                creator = user,
                image = found_image
            )
            preexisting_like.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except models.Like.DoesNotExist:

            new_like = models.Like.objects.create(
                creator = user,
                image = found_image
            )

            new_like.save()

            return Response(status=status.HTTP_201_CREATED)