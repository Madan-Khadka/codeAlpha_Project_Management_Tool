from django.urls import path

from .views import (
    login_view,
    register_view,
    logout_view,
    dashboard,
)


urlpatterns = [

    # Login
    path(
        "login/",
        login_view,
        name="login"
    ),

    # Register
    path(
        "register/",
        register_view,
        name="register"
    ),

    # Logout
    path(
        "logout/",
        logout_view,
        name="logout"
    ),

    # Dashboard
    path(
        "dashboard/",
        dashboard,
        name="dashboard"
    ),
]