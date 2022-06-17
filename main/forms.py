from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import models
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    # phone = models.CharField("Номер телефона", max_length=20, blank=True)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'phone')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'phone')
