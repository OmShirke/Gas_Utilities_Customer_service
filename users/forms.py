from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile

class EditUserForm(UserChangeForm):
    password = None  # Disable password field if not needed for edit

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['address', 'phone_number']

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Create Profile for the user without customer_id
            UserProfile.objects.create(user=user)
        return user