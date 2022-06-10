from email.message import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
import random
import string
from .models import Short_url
import uuid
from django.utils import timezone
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'shortner/home.html')


def createurl(request):
    if request.method == 'POST':
        # slug = ''.join(random.choice(string.ascii_letters)for x in range(10))
        url = request.POST["url"]
        expiration_date = request.POST['expiration_date']
        slug = str(uuid.uuid4())[:5]
        new_url = Short_url(url=url, slug=slug, expiration_date=expiration_date)
        new_url.save()
        
        messages.success(request,f'A new shortned link has created! {"localhost:8000/"+slug}')
        return redirect('success')



# def exit(request, slug):
#     url = Short_url.objects.get(slug=slug)
#     return redirect(url.url)

  

def manage(request):
    urls = Short_url.objects.all().order_by('-id')
    for data in urls:
        if data.expiration_date < timezone.now():
            send_mail(subject="Link has been expired", 
            message='Some link has been expired visit the site to confirm',
             from_email='isayaelib@gmail.com', recipient_list=[request.user.email,],fail_silently=True)
    

    context = {
        'urls':urls
    }
    return render(request, 'shortner/manage.html', context)



def profile(request):
    if request.method == 'POST':
        uform = userForm(request.POST, instance=request.user)
        pform = profileForm(request.POST, request.FILES, instance=request.user.profile)
      
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
           
            messages.success(request, f"Succesful updated profile")
            return redirect('manage')
    else:
        uform = userForm(instance=request.user)
        pform = profileForm(instance=request.user.profile)
     
    context = {
        'pform':pform,
        'uform':uform,
       
    }
    return render(request, 'shortner/profile.html', context)


def success(request):
    return render(request, 'shortner/success.html')


def update_url(request, slug):
    url = Short_url.objects.get(slug=slug)
    if request.method == 'POST':
        url.url = request.POST['url']
        url.slug = url.slug
        url.save()
        messages.success(request, 'Link updated successful')
        return redirect('manage')
    context = {
        'data':url
    }
    return render(request, 'shortner/edit.html', context)

def disable_url(request, slug):
    url = Short_url.objects.get(slug=slug)
    url.disabled = True
    url.save()
    messages.success(request, 'Link updated successful')
    return redirect('manage')
 


def delete_url(request, id):
    url = Short_url.objects.get(id=id)
    url.delete()
    return redirect('manage')

