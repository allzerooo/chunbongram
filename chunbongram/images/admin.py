from django.contrib import admin
from . import models

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):

    # 오브젝트에 접근하는 링크를 변경
    list_display_links = (
        'location',
        'caption',
    )
    
    # 검색바와 대상
    search_fields = (
        'location',
        'caption',
    )

    list_filter = (
        'location',
        'creator',
    )

    list_display = (
        'file',
        'location',
        'caption',
        'creator',
        'created_at',
        'updated_at',
    )


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    
    list_display = (
        'creator',
        'image',
        'created_at',
        'updated_at',
    )


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    
    list_display = (
        'message',
        'creator',
        'image',
        'created_at',
        'updated_at',
    )