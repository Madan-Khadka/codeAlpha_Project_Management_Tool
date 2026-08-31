from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form used to add comments to tasks.
    """

    class Meta:

        model = Comment

        fields = [
            "content"
        ]

        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Write a comment...",
                    "rows": 3,
                }
            )
        }