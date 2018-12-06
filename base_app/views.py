from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View,TemplateView
from .forms import UserForm, linkform
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth import login,logout,authenticate
import pyAesCrypt
from .models import AppUser
from django.contrib.auth.models import User



bufferSize = 64 * 1024


class IndexView(TemplateView):
    template_name = 'index.html'


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request, 'register.html', {'user_form':user_form,'registered':registered})     



def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username= username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('base_app:main'))
            else:
                return HttpResponse("Account Not active")
        
        else:
            print("Well you Failed to login")

            return HttpResponse("Invalid Login Details")

    else:
        return render(request, 'login.html')


@login_required
def mainpage(request):
    
    return render(request, 'loggedindex.html')

@login_required
def trainpage(request):
    return render(request, 'trainpage.html')
    
def testpage(request):
    return render(request, 'testpage.html')


@login_required
def encrypt(request):
    if request.method=='POST':
        
        password = request.user.appuser.key
        uploaded_file=request.FILES['upfile']
        # print(uploaded_file.name)
        pyAesCrypt.encryptFile(uploaded_file.name, "data.txt.aes", password, bufferSize)
        # pyAesCrypt.decryptFile("data.txt.aes", "dataout.txt", password, bufferSize)

    return HttpResponseRedirect(reverse('base_app:main'))
        
        
def decryptpage(request):
    if request.method=='POST':
        password = request.user.appuser.key
        uploaded_file=request.FILES['document']
        # print(uploaded_file.name)
        pyAesCrypt.decryptFile(uploaded_file.name, "dataout.txt", password, bufferSize)
        return HttpResponseRedirect(reverse('base_app:main'))

    return render(request, 'decryptpage.html')
