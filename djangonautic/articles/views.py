from django.http import HttpResponse
from django.shortcuts import render
from .models import Article



def article_list(request):
	# return HttpResponse('homepage')
	articles = Article.objects.all().order_by('date')
	return render(request, 'articles/article_list.html', {'articles':articles})
	# return render(request, )


# def about(request):
# 	# return HttpResponse('about')
# 	return render(request, 'about.html')
