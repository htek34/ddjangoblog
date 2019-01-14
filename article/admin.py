from django.contrib import admin

from .models import Comment
from .models import Article



# Register your models here.

admin.site.register(Comment)

@admin.register(Article)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]
    list_display_links =  ["title","author","created_date"]
    search_fields =["title"]

    list_filter = ["created_date","author"]

    list_per_page = 5
    list_max_show_all = 25


    class Meta:
        model = Article

