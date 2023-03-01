from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.

def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    context = {
        'text': text,
        'word_amounts': amount_of_words,
    }
    return render(request, 'counter.html', context)