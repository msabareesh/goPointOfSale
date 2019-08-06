from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html', {'name' : 'Sabareesh'})

def add(request):
    a1=int(request.POST['num1'])
    a2=int(request.POST['num2'])
    result=a1+a2
    return render(request, 'result.html', {'result':result})

