from django.shortcuts import render
from django.http import HttpResponse

# views.py

# Add this cats list below the imports
cats = [
  {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
  {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
]

# Create your views here.
def home(request):
    # return HttpResponse('hello')
    return render(request, 'cats/home.html')

def about(request):
    return render(request, 'cats/about.html')

def cats_index(request):
    # passing data extremely close to ejs
    return render(request, 'cats/index.html', {
        'cats' : cats
    })