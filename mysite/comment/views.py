from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article
from .models import Comment
from .forms import CommentForm


def article_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # commit=false 表示并不保存到数据库中
            comment.article = article  # 与被评论的文章关联
            comment.save()
            return redirect(article)  # 重定向到 article 的详情页，实际上当 redirect 函数接收一个模型的实例时，它会调用这个模型实例的 get_absolute_url 方法，
        else:
            comment_list = article.comment_set.all()  # post.comment_set.all() 反向查询全部评论。
            context = {'article': article,
                       'form': form,
                       'comment_list': comment_list}
            return render(request, 'blog/detail.html', context=context)
    return redirect(article)
