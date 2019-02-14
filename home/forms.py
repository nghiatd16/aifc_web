from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *


class MemberCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Member
        fields = ('username', 'gen')


class MemberChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = Member
        fields = ('username', 'gen')
