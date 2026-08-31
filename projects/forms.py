from django import forms
from django.contrib.auth.models import User

from .models import Project


class ProjectForm(forms.ModelForm):
    """
    Form used to create and edit projects.
    """

    class Meta:

        model = Project

        fields = [
            "name",
            "description",
        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter project name",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Describe your project",
                    "rows": 5,
                }
            ),
        }


class MemberForm(forms.Form):
    """
    Form for adding an existing user
    to a project.
    """

    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter username",
            }
        )
    )

    def clean_username(self):

        username = self.cleaned_data["username"].strip()

        try:
            user = User.objects.get(
                username=username
            )

        except User.DoesNotExist:

            raise forms.ValidationError(
                "User with this username does not exist."
            )

        return user