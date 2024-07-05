from django.shortcuts import render,redirect
from django.views.generic import ListView,DeleteView
from django.contrib import messages
from .models import *
import re  
from django.core.mail import EmailMessage


  



def validate_email(email):  
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):  
        return True  
    return False  


class AllBlogsView(ListView):
    model = Blogs
    template_name = 'allBlogs.html'

class BlogDetailView(DeleteView):
    model = Blogs
    template_name = 'details.html'



def homeview(request):
    blogs = Blogs.objects.filter(is_atHome=True)
    stories = Stories.objects.all()
    context = {'blogs':blogs,'stories':stories}
    return render(request, 'home.html',context=context)
def aboutfounderview(request):
    return render(request, 'about-founder.html')
def aboutusview(request):
    stories = Stories.objects.all()
    context = {'stories':stories}
    return render(request, 'aboutus.html',context=context)
def serviceview(request):
    return render(request, 'service.html')
def contactusview(request):
    return render(request, 'contactus.html')


def getmails(request):
    if request.method =="POST":
        mail = request.POST.get('email')
        if validate_email(mail):
            mails,created = Getmails.objects.get_or_create(email = mail)
            if created:
                messages.add_message(request, messages.SUCCESS, "Thank you.. we will contact you soon")
                
            else:
                messages.add_message(request, messages.WARNING, "You already in our contact list")
        else:
            messages.add_message(request, messages.INFO, "Enter a vaild emial address")
   
    return redirect(request.META.get('HTTP_REFERER'))

def getcontactus(request):
    print(request.POST)
    
    email = request.POST.get('email')
    
    if validate_email(email):
        name = request.POST.get('full_name')
        number = request.POST.get('phone_number')
        business = request.POST.get('business')
        message = request.POST.get('message')
        sendemail = EmailMessage(f"New enquiry from ATB web {name}",
        f"name:{name}\n business:{business} \n mobile:{number} \n message: {message}",
        "mail@accountiko.in",
        [email],
        )
        sendemail.send()
        messages.add_message(request, messages.SUCCESS, "Thank you.. we will contact you soon")
    else:
        messages.add_message(request, messages.INFO, "Enter a vaild emial address")

    return redirect(request.META.get('HTTP_REFERER'))
