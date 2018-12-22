from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from chunbongram.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()

# 나는 user를 업데이트 할 때 사용하는 폼이 없네..

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    # followers, following에는 ManyToManyField가 입력되어 있고
    # User 자신에게 연결되어 있다
    # 따라서 admin panel User 탭에서 followers, following은 다수를 선택할 수 있게 보여진다
    fieldsets = (("User", {"fields": ("name", "followers", "following", "profile_image")}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]
