from django.contrib import admin
from .models import Category, Tag, Article
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'last_modified_time', 'category']
    filter_horizontal = ['tags', ]
    # 在admin中ManyToManyField本来不可以修改，
    # 在ModelAdmin.filter_horizontal中添加ManyToManyField后，相应位置上的tag标签就可以编辑了


admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
