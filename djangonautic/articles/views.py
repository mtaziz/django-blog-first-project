from django.http import HttpResponse
from django.shortcuts import render
from .models import Article



def article_list(request):
	# return HttpResponse('homepage')
	articles = Article.objects.all().order_by('date')
	return render(request, 'articles/article_list.html', {'articles':articles})
	# return render(request, )

def article_detail(request, slug):
	# return HttpResponse(slug)
	article = Article.objects.get(slug=slug)
	return render(request, 'articles/article_detail.html', {'article':article})

# def about(request):
# 	# return HttpResponse('about')
# 	return render(request, 'about.html')
