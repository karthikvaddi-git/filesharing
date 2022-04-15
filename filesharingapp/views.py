from django.shortcuts import render
from django.http import HttpResponse
from .models import upload
# Create your views here.
def index(request):
    return render(request,"index.html")


def filesharing(request):
    print(request.POST)
    print(request.FILES['myfile'])
    u=upload(filedata=request.FILES['myfile'])
    u.save()




    return HttpResponse(request.POST)

