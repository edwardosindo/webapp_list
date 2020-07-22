import requests
from django.shortcuts import render
from bs4 import BeautifulSoup

# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    print(search)
    staff_for_frontend = {
        'search': search
    }
    return render(request, 'myapp/new_search.html', staff_for_frontend)
