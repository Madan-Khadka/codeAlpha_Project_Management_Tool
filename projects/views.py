from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProjectForm
from .models import Project


# ============================================================
# PROJECT LIST / DASHBOARD
# ============================================================
@login_required
def project_list(request):
    """
    Display projects where the logged-in user is:
    - Owner
    - OR member
    """

    projects = Project.objects.filter(
        members=request.user
    ).distinct()

    return render(
        request,
        "dashboard.html",
        {
            "projects": projects,
        }
    )


# ============================================================
# PROJECT DETAIL
# ============================================================
@login_required
def project_detail(request, project_id):
    """
    Display one project and its information.
    """

    # Find the requested project
    project = get_object_or_404(
        Project,
        id=project_id
    )

    # Check whether current user is owner/member
    if (
        project.owner != request.user
        and not project.members.filter(
            id=request.user.id
        ).exists()
    ):
        messages.error(
            request,
            "You are not a member of this project."
        )

        return redirect("dashboard")

    return render(
        request,
        "project.html",
        {
            "project": project,
        }
    )


# ============================================================
# CREATE PROJECT
# ============================================================
@login_required
def create_project(request):
    """
    Create a new project.
    """

    if request.method == "POST":

        form = ProjectForm(request.POST)

        if form.is_valid():

            # Create project object without saving immediately
            project = form.save(commit=False)

            # Logged-in user becomes project owner
            project.owner = request.user

            # Save project into database
            project.save()

            # Owner is automatically added as a member
            project.members.add(request.user)

            messages.success(
                request,
                "Project created successfully!"
            )

            # IMPORTANT:
            # Redirect to the newly created project's detail page.
            return redirect(
                "project_detail",
                project_id=project.id
            )

    else:

        form = ProjectForm()

    # IMPORTANT:
    # Create Project page uses a separate template.
    return render(
        request,
        "create_project.html",
        {
            "form": form,
        }
    )