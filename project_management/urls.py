from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


# ============================================================
# HOME VIEW
# ============================================================
def home(request):
    """
    Redirect users from "/" to login page.
    """

    return redirect("login")


# ============================================================
# URL PATTERNS
# ============================================================
urlpatterns = [

    # Django admin
    path(
        "admin/",
        admin.site.urls
    ),

    # Homepage
    path(
        "",
        home,
        name="home"
    ),

    # Accounts
    path(
        "accounts/",
        include("accounts.urls")
    ),

    # Projects
    path(
        "projects/",
        include("projects.urls")
    ),

    # Tasks
    path(
        "tasks/",
        include("tasks.urls")
    ),

    # Comments
    path(
        "comments/",
        include("comments.urls")
    ),
]