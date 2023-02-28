from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        'name': 'Haruto',
        'age': 25,
        'nationality': 'Japan'
    }
    return render(request, 'index.html', context)