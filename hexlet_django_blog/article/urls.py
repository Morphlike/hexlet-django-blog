from django.urls import path
from django.views import View
from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import IndexView

urlpatterns = [
    path('<str:tags>/<int:article_id>', IndexView.as_view(), name='article'),
    path('', views.index)
]