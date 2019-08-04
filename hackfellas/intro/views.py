from django.shortcuts import render, redirect

from .forms import RegistrationForm
# Create your views here.




def index(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False) # commit=False - means that user wouldn't save yet

            new_user.set_password(form.cleaned_data['user_password'])

            new_user.save()
            return redirect('index')

    else:
        form = RegistrationForm()
        return render(request=request,
                      template_name='intro/index.html',
                      context={'form': form})

def user_login(request):
    pass
