from django.contrib import admin

from .models import Notification, Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "owner",
        "created_at",
    )

    search_fields = (
        "name",
        "description",
        "owner__username",
    )

    filter_horizontal = (
        "members",
    )


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "message",
        "is_read",
        "created_at",
    )

    list_filter = (
        "is_read",
        "created_at",
    )