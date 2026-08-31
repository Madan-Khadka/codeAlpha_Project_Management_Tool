from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

from projects.models import Project


# ============================================================
# LOGIN VIEW
# ============================================================
def login_view(request):
    """
    Handles user login.

    User enters username and password.
    If credentials are correct, user is redirected to dashboard.
    """

    # If user is already logged in, go directly to dashboard.
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate user using Django's authentication system.
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            # Create login session.
            login(request, user)

            messages.success(
                request,
                "Login successful!"
            )

            return redirect("dashboard")

        else:

            messages.error(
                request,
                "Invalid username or password."
            )

    return render(request, "login.html")


# ============================================================
# REGISTER VIEW
# ============================================================
def register_view(request):
    """
    Creates a new user account.
    """

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        # Check all fields.
        if not username or not email or not password:

            messages.error(
                request,
                "Please fill all required fields."
            )

            return render(
                request,
                "register.html"
            )

        # Check password confirmation.
        if password != password2:

            messages.error(
                request,
                "Passwords do not match."
            )

            return render(
                request,
                "register.html"
            )

        # Check whether username already exists.
        if User.objects.filter(
            username=username
        ).exists():

            messages.error(
                request,
                "Username already exists."
            )

            return render(
                request,
                "register.html"
            )

        # Create new user.
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(
            request,
            "Account created successfully. Please login."
        )

        return redirect("login")

    return render(request, "register.html")


# ============================================================
# LOGOUT VIEW
# ============================================================
def logout_view(request):
    """
    Logs out the current user.
    """

    logout(request)

    messages.success(
        request,
        "You have been logged out."
    )

    return redirect("login")


# ============================================================
# DASHBOARD VIEW
# ============================================================
def dashboard(request):
    """
    Displays projects belonging to the logged-in user.
    """

    # Dashboard requires authentication.
    if not request.user.is_authenticated:
        return redirect("login")

    # Get projects where the current user is owner.
    owned_projects = Project.objects.filter(
        owner=request.user
    )

    # Get projects where the current user is a member.
    member_projects = Project.objects.filter(
        members=request.user
    )

    # Combine both querysets without duplicates.
    projects = (
        owned_projects | member_projects
    ).distinct()

    context = {
        "projects": projects,
    }

    return render(
        request,
        "dashboard.html",
        context
    )