from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm, CommentForm
from .models import Article


# Create your views here.

def index(request):
    articles = Article.objects.order_by('-pk')

    context = {
        'articles' : articles
    }

    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user 
            article.save()
            return redirect('articles:index')
    else: 
        article_form = ArticleForm()
    
    context = {
        'article_form': article_form
    }
    
    return render(request, 'articles/form.html', context=context)