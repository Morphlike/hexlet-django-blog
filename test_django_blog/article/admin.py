from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'timestamp') # Перечисляем поля, отображаемые в таблице списка статей
    search_fields = ['name', 'body'] # Добавляем поисковую форму по тегам
    list_filter = (('timestamp', DateFieldListFilter),) # Перечисляем поля для фильтрации
