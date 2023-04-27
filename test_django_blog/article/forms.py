from django import forms # Импортируем формы Django
from django.forms import ModelForm

from .models import Article, ArticleComment


class ArticleCommentForm(ModelForm):
    class Meta:
        model = ArticleComment
        fields = ['content']


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']
