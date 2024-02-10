from django import forms
from .models import d

class SignUpForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = d
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'confirm_password', 'address_line1', 'city', 'state', 'pincode', 'profile_picture']
        widgets = {
            'password': forms.PasswordInput,
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Password and confirm password do not match.")

        

