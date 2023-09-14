from django.shortcuts               import render, redirect
from django.contrib.auth            import authenticate, login, logout
from django.contrib                 import messages
from django.contrib.auth.decorators import login_required
from rest_framework                 import viewsets
from .forms                         import PostForm
from .models                        import Post
from .serializers                   import PostSerializer
# import openai

# Create your views here.
def board_admin(request):
    return render(request, 'board-admin.html')

# login
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, "Oops! Try Again...")
            return redirect('login')

    else:
        return render(request, 'login.html')

# logout
def logout_user(request):
    logout(request)
    messages.success(request, "Hey, you logged out! Please Try Again...")
    return redirect('/')

# post_list
def board_client(request, topic=None):

    if topic:
            main = Post.objects.all().filter(topic=topic).order_by('-views').first()
            posts = Post.objects.filter(topic=topic).exclude(id=main.id).order_by('-views')
    else:
        main = Post.objects.all().order_by('-views').first()
        posts = Post.objects.all().exclude(id=main.id).order_by('-views')
        
    content = {
        'main': main,
        'posts': posts,
    }
    
    return render(request, 'board-client.html', content)


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

def board(request, topic=None, pk=None):
    try:
        if topic:
            main_post = Post.objects.filter(topic=topic).order_by('-create_at').first()
            recommended_posts = Post.objects.filter(topic=topic).exclude(id=main_post.id).order_by('-create_at')[:2]
        else:
            main_post = Post.objects.order_by('-create_at').first()
            recommended_posts = Post.objects.exclude(id=main_post.id).order_by('-create_at')[:2]
    except:
        main_post = None
        recommended_posts = None
    context = {
        'main_post': main_post,
        'recommended_posts': recommended_posts,
    }

    return render(request, 'board.html', context)
            

# def board(request):
#     posts = Post.objects.all().order_by('-create_date')
#     return render(request, 'board.html', {'posts': posts})


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-views')
    serializer_class = PostSerializer
