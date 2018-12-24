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

    def post(self, request, id, format=None):

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
            # 존재하면 삭제
            # preexisting_like.delete()
            # post 에서는 삭제를 할 수 없음

            # 존재하면 새로운 좋아요를 생성하지 않겠다
            return Response(status=status.HTTP_304_NOT_MODIFIED)

        except models.Like.DoesNotExist:
            # 해당 좋아요가 존재하지 않으면 생성
            new_like = models.Like.objects.create(
                creator = user,
                image = found_image
            )

            new_like.save()

            return Response(status=status.HTTP_201_CREATED)


class UnLikeImage(APIView):

    def delete(self, request, id, format=None):

        user = request.user

        try:
            found_image = models.Image.objects.get(id=id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            preexisting_like = models.Like.object.get(
                creator = user,
                image=found_image
            )
            preexisting_like.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except models.Like.DoesNotExist:

            return Response(status=status.HTTP_304_NOT_MODIFIED)


class CommentOnImage(APIView):

    def post(self, request, id, format=None):
    
        # base.py 에서 CSRF_COOKIE_HTTPONLY = False 로 바꿔야 동작함
        # fron-end 에서 back-end 로 데이터 받아오기
        # print(request.data)

        user = request.user

        try:
            found_image = models.Image.objects.get(id=id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.CommentSerializer(data=request.data)

        # CommentSerializer 는 id, message, creator 3 필드를 가지는데
        # id 는 바꿀 수 없고, creator 는 read_only 이기 때문에 message 만 찾는다
        # 따라서 {"message" : "hello"} 만 보내줘도 되는 것
        # 그렇기 때문에 serializer 는 유효함 = is_valid()

        if serializer.is_valid():

            # print('im valid')

            # comment model 은 message, creator, image 필드를 가짐
            # 따라서 모델 필드를 채워 저장
            serializer.save(creator=user, image=found_image)

            # message 필드와 함께 댓글을 생성한다는 뜻
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        else:

            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Comment(APIView):

    def delete(self, request, id, format=None):

        user = request.user

        try:
            # id 는 url 의 comment id 와 같고, creator 는 현재 삭제를 요청하는 유저와 같아야
            # 따라서 다른 사람의 댓글을 삭제할 수 없음
            comment = models.Comment.objects.get(id=id, creator=user)
            comment.delete()
            return Response(status.HTTP_204_NO_CONTENT)
        except models.Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class Search(APIView):

    def get(self, request, format=None):

        hashtags = request.query_params.get('hashtags', None)

        print(hashtags)