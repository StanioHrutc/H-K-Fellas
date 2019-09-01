from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email


class FormValidators(object):

    @staticmethod
    def validate_name(field, field_name):
        if len(field) > 4:
            try:
                some_name = int(field)
                raise forms.ValidationError('{0} should contain at least 1 character'.format(field_name))
            except ValueError:
                return field
        else:
            raise forms.ValidationError('{0} should contain 4 and more characters'.format(field_name))

    @staticmethod
    def validate_password(password):
        if len(password) >= 6:
            try:
                is_numb = int(password)
                raise forms.ValidationError('Password must contain at least one char')
            except ValueError:
                print('passwords are correct')
                return password

        else:
            print('password not match')
            raise forms.ValidationError('Password must contain 6 or more characters')

    @staticmethod
    def validate_confirmation(password, confirm):
        if password == confirm:
            return FormValidators.validate_password(password=password)
        else:
            print('password not match')
            raise forms.ValidationError('Password do not match')

    @staticmethod
    def validate_email(email):
        try:
            validate_email(email)
        except forms.ValidationError:
            print('email error')
            raise forms.ValidationError('Incorrect email, please try again')

        return email


class RegistrationForm(forms.Form):
    # fields of our form
    password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Password',
        'type': 'password',
        'class': 'input form-control',
        'id': 'input-password',
        'required': True,
        'autocomplete': 'off'
    }))

    confirm = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Confirm your password',
        'type': 'password',
        'class': 'input form-control',
        'id': 'input-confirm',
        'required': True,
        'autocomplete': 'off'
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'type': 'email',
        'class': 'input form-control',
        'id': 'input-email',
        'required': True,
        'autocomplete': 'off'
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Name',
        'type': 'text',
        'class': 'input form-control',
        'id': 'input-name',
        'required': True,
        'autocomplete': 'off'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'User name',
        'type': 'text',
        'class': 'input form-control',
        'id': 'input-username',
        'required': True,
        'autocomplete': 'off'
    }))

    # meta information about model which we are working with, and related fields

    def clean_confirm(self):
        ''' method for password validation '''

        password  = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm')

        print(password, password2)

        return FormValidators.validate_confirmation(password=password, confirm=password2)

    def clean_email(self):
        ''' method for email validation '''

        email = self.cleaned_data.get('email')

        FormValidators.validate_email(email=email)

    def clean_name(self):
        ''' method for name validation '''

        name = self.cleaned_data('first_name')

        for char in FormValidators.validate_name(name, 'Name'):
            if type(char) == int:
                raise forms.ValidationError('Name should not contain a number')
        return name

    def clean_user_name(self):
        ''' method for user name validation '''

        user_name = self.cleaned_data('username')

        FormValidators.validate_name(user_name, 'User name')


class LoginForm(forms.Form):

    password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Password',
        'type': 'password',
        'class': 'input form-control',
        'id': 'password',
        'required': True
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'User name',
        'type': 'text',
        'class': 'input form-control',
        'id': 'username',
        'required': True
    }))

    def clean_password(self):
        password = self.cleaned_data['password']

        return FormValidators.validate_password(password=password)

    def clean_username(self):
        username = self.cleaned_data['username']

        return FormValidators.validate_name(field=username, field_name='Name')
