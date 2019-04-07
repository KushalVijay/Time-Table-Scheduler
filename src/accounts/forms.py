from django import forms
from django.contrib.auth import get_user_model
from .models import register,login_page,admin_login

User = get_user_model()

class LoginForm(forms.ModelForm):

    class Meta:
        model = login_page
        fields = "__all__"

class AdminLoginForm(forms.ModelForm):

    class Meta:
        model = admin_login
        fields = "__all__"


class RegisForm(forms.ModelForm):

    class Meta:
        model = register
        fields = "__all__"

    def clean_username(self):

        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username
    def clean_email(self):

        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is taken")
        return email

    def clean(self):

        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password2 != password:
            raise forms.ValidationError("Passwords must match")
        return data

