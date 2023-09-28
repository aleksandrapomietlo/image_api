from django.contrib.auth.forms import UserCreationForm

from users.models import UserAccount


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = UserAccount
        fields = UserCreationForm.Meta.fields