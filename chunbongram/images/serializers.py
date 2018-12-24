# rest_framework은 pipenv install djangorestframework로 설치한 앱
from rest_framework import serializers
from . import models
from chunbongram.users import models as user_models


class SmallImageSerializer(serializers.ModelSerializer):
    
    """ Used for the notifications """

    class Meta:
        model = models.Image
        fields = (
            'file',
        )

class CountImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'comment_count',
            'like_count'
        )

# 생성자에 대한 serializer
class FeedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = user_models.User
        fields = (
            # User 모델에는 정의되지 않았지만, AbstractUser 가 가진 username
            'username',
            'profile_image'
        )


class CommentSerializer(serializers.ModelSerializer):

    creator = FeedUserSerializer(read_only=True)

    class Meta:
        model = models.Comment
        fields = (
            'id',
            'message',
            'creator'
        )


class LikeSerializer(serializers.ModelSerializer):

    # 2. 특정 필드는 키 값이 아니라 serizalizer라고 알려줌
    # 3. 따라서, 키 값 대신 serialize 된 오브젝트가 출력됨
    #image = ImageSerializer()

    class Meta:
        model = models.Like
        # 1. 모든 필드를 가져오는데
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):

    # 2. _set 도 nested serializer 를 적용
    # 3. _set 은 related_name으로 찾기 때문에 related_name을 사용
    comments = CommentSerializer(many=True)
    # like_count를 추가하면서 likes 는 serialize 할 필요가 없어짐
    #likes = LikeSerializer(many=True)
    creator = FeedUserSerializer()

    class Meta:
        model = models.Image
        # 1. fileds = '__all__' 에는 _set과 같이 모델에 숨겨진 field를 가져올 수 없기 때문에 이렇게 나열해줘야 한다
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments',
            # image model 안에 있는 def()
            'like_count',
            'creator'
        )