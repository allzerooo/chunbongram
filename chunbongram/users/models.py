# 장고 user 모델을 디폴트로 사용하고 있다. AbstractUser는 models에서 확장된 것
# 장고 user 모델을 디폴트로 사용하고 있기 때문에 admin 패널도 슈퍼유저로 들어갈 수 있는 것
# setting > base에 AUTH_USER_MODEL = 'users.User'라고 설정한 것은 장고 user 모델만으로는 부족하기 때문이다.
# 예를 들어, bio, phone 등이 추가적으로 필요하다
from django.contrib.auth.models import AbstractUser
# from django.db.models import CharField
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

# 쿠키커터가 생성해 준 User class
@python_2_unicode_compatible
class User(AbstractUser):

    """ User Model """

    # constant
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified', 'Not specified')
    )

    # First Name and Last Name do not cover name patterns
    # around the globe.
    # name은 AbstractUser가 가지고 있는 것
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    # 밑에 있는 것들은 내가 만든 변수들
    profile_image = models.ImageField(null=True)
    website = models.URLField(null=True)
    bio = models.TextField(null=True)
    phone = models.CharField(max_length=140, null=True)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
    followers = models.ManyToManyField("self", blank=True)
    following = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
