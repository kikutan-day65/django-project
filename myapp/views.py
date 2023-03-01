from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.

def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})


def register(request):
    
    # check if the POST method is used or not, and take all info if yes 
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if password and password2 is same
        if password == password2:

            # check if email is already registered
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            
            # check if username is already registered
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            
            # create new user successfully
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save() # save information
                
                return redirect('login')
            
        else:
            messages.info(request, 'Password Not The Same')
            return redirect('register')
    
    else:
        return render(request, 'register.html')


def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    context = {
        'text': text,
        'word_amounts': amount_of_words,
    }
    return render(request, 'counter.html', context)