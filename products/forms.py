from django import forms
from .models import Package
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['title', 'description', 'price', 'expiry_date','image']



class SignUpForm(UserCreationForm):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('vendor', 'Vendor'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            role = self.cleaned_data['role']
            Profile.objects.update_or_create(user=user, defaults={'role': role})
        return user
