from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from apps.users.models import CustomUser


class CustomUsercreationFrom(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email")
        error_class = "error"


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email")
        error_class = "error"
