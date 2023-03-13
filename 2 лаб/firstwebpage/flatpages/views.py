from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'static_handler.html')
def hello(request):
    return HttpResponse(u'Hello world', content_type='text/plain')
# Create your views here.
