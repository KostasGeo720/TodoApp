from datetime import date
from django.forms import forms
from main.accounts.models import Profile

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birth_date', 'email', 'gender']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'gender': forms.Select(choices=Profile.GENDER_CHOICES),
        }
    def calculate_age(self, birth_date):
        if birth_date:
            today = date.today()
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            return age
        return None
        
    def save(self, commit=True):
        profile = super().save(commit=False)
        profile.age = self.calculate_age(profile.birth_date)
        if commit:
            profile.save()
        return profile