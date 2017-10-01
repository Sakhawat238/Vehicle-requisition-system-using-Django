from django import forms
from django.contrib.auth.models import User
from .models import RentData


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']


class RentForm(forms.ModelForm):

    class Meta:
        model = RentData
        fields = ['source', 'destination', 'start', 'end', 'carname', 'ccno']