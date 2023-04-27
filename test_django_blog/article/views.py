from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.forms import ModelForm
from django.contrib import messages

from .models import Article
from .forms import ArticleForm


class IndexView(View):
 
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:10]
        return render(request, 'article/index.html', context={
            'articles': articles,
        })
    

class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'article/show.html', context={
            'article': article,
        })


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'article/create.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The article has been added!')
            return redirect('articles')
        return render(request, 'article/create.html', {'form': form})


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'article/update.html', {'form': form, 'article_id':article_id})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'The article has been updated!')
            return redirect('articles')
        return render(request, 'article/update.html', {'form': form, 'article_id':article_id})


class ArticleFormDestroyView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
            messages.success(request, 'The article has been deleted!')
        return redirect('articles')
