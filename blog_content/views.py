from django.shortcuts import render
from .models import Category, Tag, Post, Comment, Author

# Create your views here.

def index(request):
	context = {
		'posts': Post.objects.all(),
		'categories': Category.objects.all(),
		'tags': Tag.objects.all(),
		'author': Author.objects.all(),
	}

	return render(request, 'blog_content/index.html', context)


def details(request, slug):
	pass


def contact(request):
	pass


def archives(request):
	pass


def categories(request):
	pass


def get_posts_for_tag(request, tag):
	pass


def get_post_for_category(request, category):
	pass
