from django.urls import path
from . import views

app_name = "images"
urlpatterns = [
    path("", view=views.Images.as_view(), name="images"),
    path("<int:id>/", view=views.ImageDetail.as_view(), name="image_detail"),
    # 좋아요의 작동 방법은 /images/<image_id>/like or /images/<image_id>/unlike
    # url 에서 id 를 가져오기
    path("<int:id>/likes/", view=views.LikeImage.as_view(), name="like_image"),
    path("<int:id>/unlikes/", view=views.UnLikeImage.as_view(), name="unlike_image"),
    path("<int:id>/comments/", view=views.CommentOnImage.as_view(), name="comment_image"),
    path("<int:image_id>/comments/<int:comment_id>", view=views.ModerateComments.as_view(), name="moderate_comments"),
    path("comments/<int:id>/", view=views.Comment.as_view(), name="comment"),
    path("search/", view=views.Search.as_view(), name="search"),
]