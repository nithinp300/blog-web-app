from django.shortcuts import render
from .models import Post

posts = [
	{
		'author': 'Nithin Pingili',
		'title': 'Blog Post 1',
		'content': 'My first post content',
		'date_posted': 'August 27, 2018'
	},
	{
		'author': 'Joe Cool',
		'title': 'Blog Post 2',
		'content': 'My second post content',
		'date_posted': 'August 28, 2018'
	}
]

# Create your views here.
def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})