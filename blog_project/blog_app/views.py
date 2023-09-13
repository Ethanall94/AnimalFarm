from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import PostForm
from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer

# Create your views here.

def board_client(request):
    return render(request, 'board-client.html')
def board_admin(request):
    return render(request, 'board-admin.html')
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            # return redirect('/board_admin') # 페이지가 두개라면..
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, "Oops! Try Again...")
            return redirect('/login')

    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "Hey, you logged out! Please Try Again...")
    return redirect('board-client')

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
