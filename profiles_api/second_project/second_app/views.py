from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<em>This is my second Application</em>")

def help(request):
    my_dict = {"insert_me":"this is the new Help page"}
    return render(request,'second_app/help.html',context = my_dict)
