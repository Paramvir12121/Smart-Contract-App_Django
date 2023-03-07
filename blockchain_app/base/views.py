from django.shortcuts import render

def mainPage(request):
    return render(request, 'base/pages/mainPage.html')

def login(request):
    return render(request, 'base/pages/login.html')

def home(request):
    return render(request, 'base/pages/home.html')