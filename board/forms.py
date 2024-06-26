from .models import Post
from django import forms
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    description = forms.CharField(min_length=3)

    class Meta:
        model = Post
        fields = ['title', 'postAuthor', 'text','postCategory']

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("description")
        name = cleaned_data.get("name")

        if name == description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data