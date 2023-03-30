from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class IndexView(View):
 
    def get(self, request, tags, article_id):
        _response = f'Статья номер {article_id}. Тег {tags}'
        return HttpResponse(_response)
    
def index(request):
    return HttpResponse('article')