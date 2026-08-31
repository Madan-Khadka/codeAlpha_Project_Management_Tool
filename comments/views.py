from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from projects.models import Notification
from tasks.models import Task

from .forms import CommentForm
from .models import Comment


@login_required
def add_comment(request, task_id):
    """
    Add a new comment to a task.
    """

    task = get_object_or_404(
        Task,
        id=task_id
    )

    # Check project membership.
    if not (
        request.user == task.project.owner
        or task.project.members.filter(
            id=request.user.id
        ).exists()
    ):

        messages.error(
            request,
            "You don't have permission."
        )

        return redirect("dashboard")

    if request.method == "POST":

        form = CommentForm(
            request.POST
        )

        if form.is_valid():

            comment = form.save(
                commit=False
            )

            comment.task = task

            comment.user = request.user

            comment.save()

            # Notify assigned user.
            if (
                task.assigned_to
                and task.assigned_to != request.user
            ):

                Notification.objects.create(
                    user=task.assigned_to,
                    project=task.project,
                    task_id=task.id,
                    message=(
                        f'{request.user.username} commented '
                        f'on "{task.title}".'
                    )
                )

            messages.success(
                request,
                "Comment added."
            )

    return redirect(
        "task_detail",
        task_id=task.id
    )


@login_required
def delete_comment(request, comment_id):
    """
    Delete own comment.
    """

    comment = get_object_or_404(
        Comment,
        id=comment_id
    )

    if comment.user != request.user:

        messages.error(
            request,
            "You can only delete your own comments."
        )

        return redirect(
            "task_detail",
            task_id=comment.task.id
        )

    task_id = comment.task.id

    if request.method == "POST":

        comment.delete()

        messages.success(
            request,
            "Comment deleted."
        )

    return redirect(
        "task_detail",
        task_id=task_id
    )