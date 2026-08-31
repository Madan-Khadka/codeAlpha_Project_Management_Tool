from django.urls import path

from .views import add_comment, delete_comment


urlpatterns = [

    # Add comment
    path(
        "task/<int:task_id>/add/",
        add_comment,
        name="add_comment"
    ),

    # Delete comment
    path(
        "<int:comment_id>/delete/",
        delete_comment,
        name="delete_comment"
    ),
]