from django.shortcuts import render
from django.utils import timezone
from .models import Article
from .models import Poem
from .models import Miscellaneous
from django.shortcuts import render, get_object_or_404
from itertools import chain
from .forms import ArticleForm
from .forms import PoemForm
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

def home_list(request):
    articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:5]
    poems = Poem.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:4]
    miscellaneouss = Miscellaneous.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:4]
    return render(request, 'blog/home_list.html', {'articles': articles,'poems': poems,'miscellaneouss': miscellaneouss})

def article_list(request):
    articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:20]
    return render(request, 'blog/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if(article.isVerified):
        return render(request, 'blog/article_detail.html', {'article': article})
    else:
        return render(request, 'blog/post_save.html')

def poem_list(request):
    poems = Poem.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:4]
    return render(request, 'blog/poem_list.html', {'poems': poems})

def poem_detail(request, pk):
    poem = get_object_or_404(Poem, pk=pk)
    if(poem.isVerified):
        return render(request, 'blog/poem_detail.html', {'poem': poem})
    else:
        return render(request, 'blog/post_save.html')

def miscellaneous_list(request):
    miscellaneouss = Miscellaneous.objects.filter(published_date__lte=timezone.now()).filter(isVerified=True).order_by('published_date')[:4]
    return render(request, 'blog/miscellaneous_list.html', {'miscellaneouss': miscellaneouss})

def miscellaneous_detail(request, pk):
    miscellaneous = get_object_or_404(Miscellaneous, pk=pk)
    return render(request, 'blog/miscellaneous_detail.html', {'miscellaneous': miscellaneous})

@csrf_exempt
def article_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.published_date = timezone.now()
            article.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'blog/article_edit.html', {'form': form})

@csrf_exempt
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.published_date = timezone.now()
            article.isverified = False
            article.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/article_edit.html', {'form': form})

@csrf_exempt
def poem_new(request):
    if request.method == "POST":
        form = PoemForm(request.POST)
        if form.is_valid():
            poem = form.save(commit=False)
            poem.published_date = timezone.now()
            poem.save()
            return redirect('poem_detail', pk=poem.pk)
    else:
        form = PoemForm()
    return render(request, 'blog/poem_edit.html', {'form': form})

@csrf_exempt
def poem_edit(request, pk):
    poem = get_object_or_404(Poem, pk=pk)
    if request.method == "POST":
        form = PoemForm(request.POST, instance=poem)
        if form.is_valid():
            poem = form.save(commit=False)
            poem.published_date = timezone.now()
            poem.isverified = False
            poem.save()
            return redirect('poem_detail', pk=poem.pk)
    else:
        form = PoemForm(instance=poem)
    return render(request, 'blog/poem_edit.html', {'form': form})