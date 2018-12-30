from django.urls import path
from . import views

# from chunbongram.users.views import (
#     user_list_view,
#     user_redirect_view,
#     user_update_view,
#     user_detail_view,
# )

# app_name = "users"
# urlpatterns = [
#     path("", view=user_list_view, name="list"),
#     path("~redirect/", view=user_redirect_view, name="redirect"),
#     path("~update/", view=user_update_view, name="update"),
#     path("<str:username>/", view=user_detail_view, name="detail"),
# ]

app_name = "users"
urlpatterns = [
    path("explore/", view=views.ExploreUsers.as_view(), name="explore_users"),
    path("<int:id>/follow/", view=views.FollowUser.as_view(), name="follow_user"),
    path("<int:id>/unfollow/", view=views.UnFollowUser.as_view(), name="unfollow_user"),
    # user_profile 이 search 보다 위에 오게 되면 user_profile 에 먼저 매칭되기 때문에 순서를 바꿈
    path("search/", view=views.Search.as_view(), name="search"),
    path("<str:username>/", view=views.UserProfile.as_view(), name="user_profile"),
    path("<str:username>/password/", view=views.ChangePassword.as_view(), name="change_password"),
    path("<str:username>/followers/", view=views.UserFollowers.as_view(), name="user_followers"),
    path("<str:username>/following/", view=views.UserFollowing.as_view(), name="user_following"),
]
