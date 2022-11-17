from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def home(request):
    return HttpResponse("Home Page")


def hi_name(request, username):
    return HttpResponse("Hi " + username)


def age(request, year):
    return HttpResponse("Age " + str(2022 - year))


def hello_view(request):

    fourseason = range(1, 5)
    p1 = {"name": "Amy", "phone": "080-1234-5789", "age": 20}
    p2 = {"name": "Jack", "phone": "070-3567-1259", "age": 30}
    p3 = {"name": "Nacy", "phone": "090-4129-6787", "age": 25}
    persons = [p1, p2, p3]
    return render(request, "hello_django.html", {
        "title": "For Template",
        "data": "Hello Django!!!",
        "seasons": fourseason,
        "persons": persons,
        "now": datetime.now()
    })

# Create your views here.
