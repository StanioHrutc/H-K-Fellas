from django import forms
from django.contrib.auth.models import User




class RegistrationForm(forms.ModelForm):
    user_password        = forms.CharField(label='your password', widget=forms.PasswordInput)
    password_confirm     = forms.CharField(label='repeat your password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['user_password'] != cleaned_data['password_confirm']:
            raise forms.ValidationError('Password do not match')
        return cleaned_data['password_confirm']
