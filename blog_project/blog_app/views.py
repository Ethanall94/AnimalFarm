from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer
from django.contrib.auth.decorators import login_required

# Create your views here.

def board_client(request):
    return render(request, 'board-client.html')
def board_admin(request):
    return render(request, 'board-admin.html')
def login(request):
    return render(request, 'login.html')

# @login_required  #로그인 시 작성할 수 있도록 설정(로그인 설정 후 활성화)
def write(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            post = form.save()
            return redirect('board')
    else:
        form = PostForm()
    return render(request, 'write.html', {'form' : form})

def board(request):
    posts = Post.objects.all().order_by('-create_date')
    return render(request, 'board.html', {'posts': posts})

# def board(request):
#     try:
#         post = Post.objects.latest('create_date')
#     except:
#         post = None
#     return render(request, 'board.html', {'post': post})


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
