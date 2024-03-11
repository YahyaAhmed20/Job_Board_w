from django.shortcuts import render

# Create your views here.


def send_messgae(request):
    return render(request,'contact/contact.html')