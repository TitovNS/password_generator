import random

from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = [chr(x) for x in range(ord('a'), ord('z') + 1)]

    if request.GET.get('uppercase'):
        characters.extend([x.upper() for x in characters])
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend([str(x) for x in range(10)])

    length = int(request.GET.get('length', 12))
    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return HttpResponse(thepassword)
