from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Mansvi 👋 This is my HTTP response")

