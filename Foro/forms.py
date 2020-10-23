from django import forms

from .models import Comment, DenunciaPost, DenunciaComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class PostReportForm(forms.ModelForm):
    class Meta:
        model = DenunciaPost
        fields = ('text',)


class CommentReportForm(forms.ModelForm):
    class Meta:
        model = DenunciaComment
        fields = ('text',)
