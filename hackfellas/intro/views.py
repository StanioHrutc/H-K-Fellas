from django.http import HttpResponse
from django.contrib import auth
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import RegistrationForm, LoginForm
# Create your views here.
from django.contrib.auth.models import User


class IntroView(View):
    template_name     = 'intro/index.html'
    registration_form = RegistrationForm()

    def get(self, request, *args, **kwargs):
        return render(request=request,
                      template_name=self.template_name,
                      context={'form': self.registration_form}
                      )

    def post(self, request, *args, **kwargs):
        self.registration_form = RegistrationForm(request.POST)

        if self.registration_form.is_valid():
            user_password = self.registration_form.cleaned_data['password']
            name          = self.registration_form.cleaned_data['first_name']
            username      = self.registration_form.cleaned_data['username']
            email         = self.registration_form.cleaned_data['email']

            if User.objects.filter(email=email).exists() or User.objects.filter(username=username):
                raise Exception('User already in db')
            else:
                new_user = User.objects.create_user(username=username,
                                                    first_name=name,
                                                    password=user_password,
                                                    email=email)
                new_user.save()

                return redirect('login')
        else:
            print('invalid form')
            return render(request=request,
                          template_name=self.template_name,
                          context={'form': self.registration_form})


class LoginView(View):
    template_name = 'intro/login.html'
    login_form    = LoginForm()

    def get(self, request, *args, **kwargs):
        return render(request=request,
                      template_name=self.template_name,
                      context={'form': self.login_form}
                      )

    def post(self, request, *args, **kwargs):
        self.login_form = LoginForm(request.POST)

        if self.login_form.is_valid():
            user_name     = self.login_form.cleaned_data['username']
            user_password = self.login_form.cleaned_data['password']

            user = auth.authenticate(username=user_name,
                                     password=user_password
                                     )

            if user is not None:
                auth.login(request=request,
                           user=user)

                return redirect('/personal/')

            else:
                return render(request=request,
                              template_name=self.template_name,
                              context={'form': self.login_form}
                              )

        else:
            print('invalid form')
            return render(request=request,
                          template_name=self.template_name,
                          context={'form': self.login_form}
                          )


