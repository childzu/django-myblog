from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Post, Comment
from .forms import NewPostForm, NewCommentForm

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    user = User.objects.first()  # get the currently logged in user
    form = NewCommentForm()
    comments = Comment.objects.all().filter(post=post.pk)
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.create_by = user
            comment.post = post
            comment.save()
        
        comments = Comment.objects.all().filter(post=post.pk)
        return render(request, 'post_detail.html', {'post': post, 'form': form, 'comments': comments})
    else:        
        return render(request, 'post_detail.html', {'post': post, 'form': form, 'comments': comments})

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