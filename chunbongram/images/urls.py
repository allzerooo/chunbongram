from django.urls import path
from . import views

app_name = "images"
urlpatterns = [
    path("", view=views.Feed.as_view(), name="feed"),
    # 좋아요의 작동 방법은 /images/<image_id>/like or /images/<image_id>/unlike
    # url 에서 id 를 가져오기
    path("<int:id>/like/", view=views.LikeImage.as_view(), name="like_image"),
    path("<int:id>/unlike/", view=views.UnLikeImage.as_view(), name="unlike_image"),
    path("<int:id>/comments/", view=views.CommentOnImage.as_view(), name="comment_image"),
    path("comments/<int:id>/", view=views.Comment.as_view(), name="comment"),
]