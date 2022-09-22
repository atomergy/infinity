from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import CustomUser

# Create your custom forms here.


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
            "avatar",
            "email",
            "username",
            "first_name",
            "last_name",
            "bio",
        )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class LoginForm(AuthenticationForm):
    remember = forms.BooleanField(required=False)  # and add the remember [me] field
