from datetime import date
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class NewUserProfileForm(UserCreationForm):
    birth_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )
    gender = forms.ChoiceField(
        choices=Profile.GENDER_CHOICES,
        required=False,
        widget=forms.Select()
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already in use.')
        return email

    def calculate_age(self, birth_date):
        if birth_date:
            today = date.today()
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            return age
        return None

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
            # Create the profile
            profile = Profile.objects.create(
                user=user,
                birth_date=self.cleaned_data.get('birth_date'),
                email=self.cleaned_data['email'],
                gender=self.cleaned_data.get('gender'),
                age=self.calculate_age(self.cleaned_data.get('birth_date'))
            )
        return user