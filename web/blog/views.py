from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
# Create your views here.

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_list(request):
	MAX_LINE = 5

	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	for i in range(len(posts)):
		posts[i].text = ''.join(posts[i].text.split('\n')[:MAX_LINE]) + '\n...'
	return render(request,'blog/post_list.html',{'posts':posts})

def portpolio_list(request):
	return render(request, 'blog/portpolio_list.html', {})

def sites(request):
	return render(request, 'blog/sites.html', {})

def index_detail(request):
	return render(request,'blog/index.html',{})
