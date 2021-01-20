from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.core.mail import send_mail, send_mass_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from sharefestsite.settings import EMAIL_HOST_USER
from allpages.forms import EmailForm
from . import forms
from .models import AllUser
from django.conf import settings
from django.contrib.auth import get_user_model

def home_view(request):
    return render(request, 'allpages/index.html')

def about_view(request):
    return render(request, 'allpages/about.html')

#def connect_view(request):
#    return render(request, 'allpages/connect.html')

def user_info(request):
    context = {}
    #ontext["dataset"] = AllUsers.objects.all()
    user = get_user_model()
    context["dataset"] = user.objects.values_list('username', 'email')
    return render(request, 'allpages/user_info.html', context)

def contact(request):
    #sub = forms.EmailForm()
    if request.method == 'GET':
        sub = EmailForm()
    else:
        sub = forms.EmailForm(request.POST)
        if sub.is_valid():
            receivers = []
            user = get_user_model()
            userList = user.objects.values_list('email')
            for user in userList:
                string = str(user)
                oldstr = string.replace('(','').replace(')','')
                newstr = oldstr.replace("'",'').replace(',','')
                receivers.append(newstr)
            subj = sub.cleaned_data['subject']
            memo = sub.cleaned_data['message']
            #recepient = str(sub['Emails'].value())
            #send_mail(subj, memo, EMAIL_HOST_USER, [recepient], fail_silently= False)
            send_mail(subj, memo, EMAIL_HOST_USER, receivers, fail_silently= False)
        return render(request, 'allpages/success.html', {'recepient': receivers})
    return render(request, 'allpages/contact.html', {'form': sub})

#def thanks(request):
 #   return HttpResponse('Thank you for your message.')

def success_view(request):
    return(request, 'allpages/success.html')

def map_view(request):
    return render(request, 'allpages/mappage.html')
    
def donate_view(request):
    return render(request, 'allpages/donate.html')

def volunteer_view(request):
    return render(request, 'allpages/volunteer.html')
