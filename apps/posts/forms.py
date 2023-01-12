from django import forms


class PostForm(forms.Form):
    content = forms.CharField(label="Содержимое", widget=forms.Textarea())
