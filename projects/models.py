from django.db import models
from django.contrib.auth.models import User


# ============================================================
# PROJECT MODEL
# ============================================================
class Project(models.Model):
    """
    Stores information about a project.

    A project has:
    - One owner
    - Multiple members
    - Name
    - Description
    - Creation date
    """

    # Project name
    name = models.CharField(
        max_length=200
    )

    # Project description
    description = models.TextField(
        blank=True
    )

    # User who created/owns the project
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="owned_projects"
    )

    # Users who are members of this project
    members = models.ManyToManyField(
        User,
        related_name="member_projects",
        blank=True
    )

    # Automatically stores project creation date/time
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    # Display project name in Django admin
    def __str__(self):
        return self.name

    # Return owner's username
    @property
    def owner_name(self):
        return self.owner.username


# ============================================================
# NOTIFICATION MODEL
# ============================================================
class Notification(models.Model):
    """
    Stores notifications for users.

    Example notifications:
    - You were added to a project.
    - A task was assigned to you.
    - Someone commented on your task.
    """

    # User who receives the notification
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications"
    )

    # Notification message
    message = models.TextField()

    # Whether user has already read the notification
    is_read = models.BooleanField(
        default=False
    )

    # Automatically stores notification creation time
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    # Display notification in admin
    def __str__(self):
        return f"{self.user.username} - {self.message[:50]}"