from django.shortcuts import render
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    
    if request.GET.get('specials'):
        characters.extend(list('!@#$%^&*()'))
    
    
    lenght = int(request.GET.get('lenght', 12))

    the_password = ''

    for _ in range(lenght):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})