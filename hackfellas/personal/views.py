from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.


def profile(request):
    return render(request=request,
                  template_name='personal/profile.html',
                  context={})


@login_required(login_url='/login')
def logout(request):
    auth.logout(request=request)
    return redirect('index')
