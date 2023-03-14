from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("<h1>Welcome to home page!!!</h1>")
    return render(request, 'home.html')

def count(request):
    ft = request.GET['fulltext']
    wl = ft.split(" ")
    wc = len(wl)
    return render(request, 'count.html', {'count': wc})
