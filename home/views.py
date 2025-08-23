from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact 
from django.contrib import messages


# Create your views here.
def index(request):
    context = {
        'variable1': "Shubh is perfect",
        'variable2': "Shubh loves sketch",
    }

    # messages.success(request, "this is test message")
    return render(request, 'index.html', context)
    # return HttpResponse("This is Homepage")

def instantcoffee(request):
    return render(request, 'instantcoffee.html')
    # return HttpResponse("This is Instant Coffee page")

def gifts(request):
    return render(request, 'gifts.html')
    # return HttpResponse("This is Gifts page")

def accessories(request):
    return render(request, 'accessories.html')
    # return HttpResponse("This is Accessories page")
def aboutus(request):
    return render(request, 'aboutus.html')
    # return HttpResponse("This is About Us page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name =name, email =email, phone = phone, desc = desc, date = datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")
    return render(request, 'contact.html')
    # return HttpResponse("This is Contact page")