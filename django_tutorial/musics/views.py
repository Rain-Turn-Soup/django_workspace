from django.shortcuts import render
def hello_view(request):
    return render(request,"hello_django.html", {
        "data": "Hello Django",
    })