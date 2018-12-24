from rest_framework import serializers
from . import models
from chunbongram.images import serializers as images_serializers


class UserProfieSerializer(serializers.ModelSerializer):

    images = images_serializers.UserProfileImagesSerializer(many=True)

    class Meta:
        model = models.User
        fields = (
            'username',
            'name',
            'bio',
            'website',
            'post_count',
            'followers_count',
            'following_count',
            # images 는 장고가 똑똑하기 때문에 해주는 것. Image Model - User Model
            'images'
        )

class ExploreUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            'id',
            'profile_image',
            'username',
            'name'
        )