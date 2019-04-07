from django import forms
from .models import faculty_info

class Infoform(forms.ModelForm):

    class Meta:
        model = faculty_info
        fields = "__all__"

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "@" in email:
            raise forms.ValidationError("Email is not valid")
        return email



