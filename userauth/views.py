from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.contrib.auth import login, authenticate, logout  
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Profile
from .forms import registerForm


# Create your views here.
def request_login(request):
    if request.method == 'POST':
       
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Successful Logged In')
            return redirect('manage')
        messages.error(request, 'Username or password is Incorrect!')
        return redirect('login')
        
    return render(request,  'userauth/login.html')


def register_request(request):
   
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                messages.error(request,'User with this email already exists, Use a different email!!')
                return redirect('register')
            else:
                user = form.save()
                user.save()
                login(request, user)
                return redirect('manage')
                
    else:
        form = registerForm()
    context = {
        'form':form
    }
 
    return render(request, 'userauth/register.html',context )



def logout_request(request):
    logout(request)
    messages.info(request,f"Logged out successful")
    return redirect('login')