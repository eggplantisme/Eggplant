from ..models import Article, Category, Tag
from django import template
from django.db.models.aggregates import Count

register = template.Library()  # 自定义模板标签


@register.simple_tag
def get_recent_article(num=5):
    return Article.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Article.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    return Category.objects.annotate(num_articles=Count('article')).filter(num_articles__gt=0)


@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_articles=Count('article')).filter(num_articles__gt=0)

