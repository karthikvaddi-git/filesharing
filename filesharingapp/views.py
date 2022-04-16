from django.shortcuts import render
from django.http import HttpResponse
from .models import upload,uploadPrivate




# Create your views here.
def index(request):



    return render(request,"index.html")


def filesharing(request):

    print(request.POST)
    if request.POST['option']=='public':
        u = upload(filedata=request.FILES['myfile'])
        u.save()
    else:
        u = uploadPrivate(filedata=request.FILES['myfile'])
        u.save()

    return HttpResponse("you are file sucessfully uploaded")








    return HttpResponse(request.POST)

