from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Welcome to Homepage!</h1>')


def blog_home(request):
    return render(request, 'home_page.html')

