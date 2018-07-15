from django.shortcuts import render
from movies.models import MovieLines
 
 
def home(request):
    movie_lines = MovieLines.objects.order_by('?')[:1] #随机获取n条记录
    return render(request, 'home.html', {'movie_lines': movie_lines, })

def about(request):
	return render(request, 'about.html', {})





