from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from account.models import Account


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Account
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Account
        fields = ('email',)