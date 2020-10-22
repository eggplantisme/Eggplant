import markdown
from django.db import models
from django.urls import reverse
from django.utils.html import strip_tags
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=70)

    body = models.TextField()
    excerpt = models.CharField(max_length=200, blank=True)

    created_time = models.DateTimeField()
    last_modified_time = models.DateTimeField()

    views = models.PositiveIntegerField(default=0)

    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    # 自定义 get_absolute_url 方法
    # reverse 后面的参数会自动匹配blog下detail路径的参数'^/(?P<pk>[0-9]+)/$'
    # 生辰路径
    def get_absolute_url(self):
        # 这里也可以通过在模板中使用<a href="{% url 'blog:detail' article.pk %}">{{article.title}}</a>
        # 来实现逆向链接获取
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_view(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        # 生成摘要
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:54]
        super(Article, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_time']
