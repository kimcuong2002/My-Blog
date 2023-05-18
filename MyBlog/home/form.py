from django import forms
import re
from django.contrib.auth.models import User


class Validate(forms.Form):
    username = forms.CharField(max_length=50, min_length=6)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(), max_length=50, min_length=6)
    confirmpassword = forms.CharField(widget=forms.PasswordInput(), max_length=50, min_length=6)

    def clean_confirmpassword(self):
        if "password" in self.cleaned_data:
            password = self.cleaned_data["password"]
            confirmpassword = self.cleaned_data["confirmpassword"]
            if password == confirmpassword and password:
                return confirmpassword
            raise forms.ValidationError("Password is not valid")

    def clean_username(self):
        username = self.cleaned_data["username"]
        if not re.search(r"^\w+$", username):
            raise forms.ValidationError("Username is not valid")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("ten tk da ton tai")

    def save(self):
        User.objects.create_user(
            username=self.cleaned_data["username"],
            email=self.cleaned_data["email"],
            password=self.cleaned_data["password"],
        )
