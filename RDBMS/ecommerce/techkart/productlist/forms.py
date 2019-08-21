from django import forms
from .models import productreviews


class productrev(forms.ModelForm):
    class Meta:
        model = productreviews
        fields = "__all__"