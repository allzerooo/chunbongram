# rest_framework은 pipenv install djangorestframework로 설치한 앱
from rest_framework import serializers
from . import models


class CommentSerializer(serializers.ModelSerializer):

    #image = ImageSerializer()

    class Meta:
        model = models.Comment
        fields = '__all__'


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
    likes = LikeSerializer(many=True)

    class Meta:
        model = models.Image
        # 1. fileds = '__all__' 에는 _set과 같이 모델에 숨겨진 field를 가져올 수 없기 때문에 이렇게 나열해줘야 한다
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments',
            'likes'
        )