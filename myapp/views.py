from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def counter(request):
    text = request.GET['text']
    amount_of_words = len(text.split())
    context = {
        'text': text,
        'word_amounts': amount_of_words,
    }
    return render(request, 'counter.html', context)