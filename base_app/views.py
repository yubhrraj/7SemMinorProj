from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from django.views.generic import View,TemplateView
from .forms import UserForm, linkform

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth import login,logout,authenticate


class IndexView(TemplateView):
    template_name = 'index.html'

# class loginView(TemplateView):
#     template_name = 'login.html'

# class RegisterView(TemplateView):
#     template_name = 'register.html'

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        link_form = linkform(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            linke = link_form.save(commit = False)
            linke.user = user
            linke.save()
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
                return HttpResponseRedirect('main')
            else:
                return HttpResponse("Account Not active")
        
        else:
            print("Well you Failed to login")

            return HttpResponse("Invalid Login Details")

    else:
        return render(request, 'login.html')


def mainpage(request):
    return render(request, 'loggedindex.html')


def trainpage(request):
    return render(request, 'trainpage.html')
    



# class LoggedIndexView(TemplateView):
#     template_name = 'loggedindex.html'

# class decryptPageView(TemplateView):
#     template_name = 'decryptpage.html'

# class trainImageView(TemplateView):
#     template_name = 'train.html'