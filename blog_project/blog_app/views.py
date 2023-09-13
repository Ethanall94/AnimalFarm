from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer

# Create your views here.

def board_client(request):
    return render(request, 'board-client.html')
def board_admin(request):
    return render(request, 'board-admin.html')
def login(request):
    return render(request, 'login.html')
def write(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post(**form.cleaned_data)
            post.save()
            return redirect('')
    else:
        form = PostForm()
    context = {
        'form' : form
    }
    return render(request, 'write.html', context)

def board(request):
    try:
        post = Post.objects.latest('create_date')
    except:
        post = None
    return render(request, 'board.html', {'post': post})


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-views')
    serializer_class = PostSerializer
