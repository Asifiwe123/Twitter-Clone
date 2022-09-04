from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

def index(request):

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()

            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.erros.as_json())

    # get all posts, limit = 20
    posts = Post.objects.all()[:20]

    #show
    return render(request, 'posts.html',
                   {'posts': posts})
def delete(request, post_id):
    post= Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

def likes(request, post_id):
    post= Post.objects.get(id=post_id)
    post.like +=1
    post.save()
    return HttpResponseRedirect('/')

def edit(request, post_id ):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():

            form.save()

            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.erros.as_json())

    # get all posts, limit = 20

    #show
    return render(request, 'edit.html',
                   {'post': post})