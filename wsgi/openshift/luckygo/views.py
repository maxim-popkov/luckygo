from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello, world. You're at the LuckyGo index.")
    return render(request, 'luckygo/index.html')

def search(request):
	# return HttpResponse("Hello, world. You're at the LuckyGo search page.")
	return render(request, 'luckygo/search.html')

def details(request, path_id):
	return render(request, 'luckygo/details.html')

def twitter(request):
	# return HttpResponse("Hello, world. You're at the LuckyGo search page.")
	return render(request, 'luckygo/twitter.html')
