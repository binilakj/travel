from django.http import HttpResponse
from django.shortcuts import render
from . models import photos
from . models import media
# Create your views here.

def app(request):
    a = photos.objects.all()
    b = media.objects.all()
    return render(request, "index.html",{'res': a,'result':b})



