from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    name_of_app = 'article'
    return render(
        request,
        'article/index.html',
        context={'name': name_of_app},
    )