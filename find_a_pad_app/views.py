from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, 'welcome.html')

def search(request):
    arguments = request.body
    return render(request, 'search.html')

def location(request):
    return render(request, 'location.html')







