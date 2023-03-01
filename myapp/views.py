from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.

def index(request):
    feature1 = Feature()
    feature1.id = 1
    feature1.name = 'HARUTO MORI'
    feature1.details = 'Japanese society'


    feature2 = Feature()
    feature2.id = 2
    feature2.name = 'YAZAN GHUNAIM'
    feature2.details = 'Jordanian society'

    feature3 = Feature()
    feature3.id = 3
    feature3.name = 'JOSE LOPEZ'
    feature3.details = 'Middle american society'

    features = [
        feature1,
        feature2,
        feature3,
    ]

    return render(request, 'index.html', {'features': features})

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    context = {
        'text': text,
        'word_amounts': amount_of_words,
    }
    return render(request, 'counter.html', context)