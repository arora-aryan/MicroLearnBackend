from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email')  # Include these fields in the form

    def clean(self):
        cleaned_data = super().clean()
        print("hi", cleaned_data)
        password = cleaned_data.get("password1")
        confirm_password = cleaned_data.get("password2")

        if password and confirm_password and password != confirm_password:
            self.add_error('password2', "Password and Confirm password do not match")

        return cleaned_data
