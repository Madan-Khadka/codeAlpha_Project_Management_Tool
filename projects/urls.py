from django.urls import path

from . import views


urlpatterns = [

    # --------------------------------------------------------
    # Project list
    # --------------------------------------------------------
    path(
        "",
        views.project_list,
        name="project_list"
    ),

    # --------------------------------------------------------
    # Create a new project
    # URL:
    # /projects/create/
    # --------------------------------------------------------
    path(
        "create/",
        views.create_project,
        name="create_project"
    ),

    # --------------------------------------------------------
    # Project detail
    # URL example:
    # /projects/1/
    # --------------------------------------------------------
    path(
        "<int:project_id>/",
        views.project_detail,
        name="project_detail"
    ),
]