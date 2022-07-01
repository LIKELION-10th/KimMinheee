from .models import Comment
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm): #django model form
    class Meta:
        model=Comment
        fields=['comment']