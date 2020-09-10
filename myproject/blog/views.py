from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Post
from .forms import NewPostForm

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def new_post(request):
    user = User.objects.first()  # get the currently logged in user
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.create_by = user
            post.save()
            return redirect('post_detail', pk=post.pk)  # Redirect to the post detail page
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {'form': form})