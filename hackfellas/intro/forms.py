from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email


class RegistrationForm(forms.Form):
    # fields of our form
    password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Password',
        'type': 'password',
        'class': 'input form-control',
        'id': 'password',
        'required': True
    }))

    confirm = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Confirm your password',
        'type': 'password',
        'class': 'input form-control',
        'id': 'confirm',
        'required': True
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'type': 'email',
        'class': 'input form-control',
        'id': 'email',
        'required': True
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Name',
        'type': 'text',
        'class': 'input form-control',
        'id': 'name',
        'required': True
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'User name',
        'type': 'text',
        'class': 'input form-control',
        'id': 'username',
        'required': True
    }))

    # meta information about model which we are working with, and related fields



    def clean_confirm(self):
        ''' method for password validation '''

        password  = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm')

        print(password, password2)

        if password == password2:
            if len(password) >= 6:
                try:
                    is_numb = int(password)
                except:
                    print('passwords are correct')
                    return password

            else:
                print('password not match')
                raise forms.ValidationError('Password must contain 6 or more characters')
        else:
            print('password not match')
            raise forms.ValidationError('Password do not match')

    def clean_email(self):
        ''' method for email validation '''
        # clean data from input fields


        email = self.cleaned_data.get('email')

        try:
            validate_email(email)
        except:
            print('email error')
            raise forms.ValidationError('Incorrect email, please try again')

        return email

    def clean_name(self):
        ''' method for name validation '''

        name = self.cleaned_data('first_name')

        try:
            x = int(name)
        except ValueError:
            raise forms.ValidationError('name should contain only characters')

        if len(name) > 4:
            for char in name:
                if type(char) == int:
                    raise forms.ValidationError('name should not contain a number')
            return name
        else:
            raise forms.ValidationError('Name should contain 4 and more characters')

    def clean_user_name(self):
        ''' method for user name validation '''

        user_name = self.cleaned_data('username')

        if len(user_name) > 4:
            try:
                name = int(user_name)
            except ValueError:
                raise forms.ValidationError('user name should contain at least 1 character')

            return user_name
        else:
            raise forms.ValidationError('User name should contain 4 and more characters')

