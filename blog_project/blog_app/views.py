from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import PostForm
from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# import openai
from django.conf import settings
# from bs4 import BeautifulSoup

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
def post_list(request, topic=None):
    try:
        if topic:
                main = Post.objects.all().filter(topic=topic).order_by('-views').first()
                posts = Post.objects.all().filter(topic=topic).exclude(id=main.id).order_by('-views')
        else:
            main = Post.objects.all().order_by('-views').first()
            posts = Post.objects.all().exclude(id=main.id).order_by('-views')

    except:
        main = None
        posts = None

    content = {
        'main': main,
        'posts': posts,
        'Animal': ["media/Aniamls/quokka.jpg", "media/Aniamls/puppy.jpg", "media/Aniamls/lesser.jpg", "media/Aniamls/fox.jpg"]
    }

    return render(request, 'post-list.html', content)

# @login_required  #로그인 시 작성할 수 있도록 설정(로그인 설정 후 활성화)

def write(request, post_id=None):
    if post_id:
        # 글 수정
        post = get_object_or_404(Post, id=post_id)
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance=post)
        else:
            form = PostForm(instance=post)
    else:
        # 글 새로 작성
        post = None
        form = PostForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            # 게시물 삭제
            if 'deleteButton' in request.POST:
                post.delete() 
                return redirect('board')

            if not form.cleaned_data.get('topic'):
                post.topic = '전체'

            if 'temporary' in request.POST:
                post.is_draft = True
            else:
                post.is_draft = False
            # 글쓴이
            post.author_id = request.user.username
            post = form.save()
            return redirect('board')
    # 임시 저장 리스트
    drafts = Post.objects.filter(is_draft=True)
    context = {'form': form, 'drafts': drafts}
    return render(request, 'write.html' if not post_id or not post else 'edit.html', context)



# 보더
def board(request, topic=None, post_id=None):

    try:
        if topic:
            main_post = Post.objects.filter(topic=topic).order_by('-create_at').first()
            main_post.views += 1
            main_post.save()
            recommended_posts = Post.objects.filter(topic=topic).exclude(id=main_post.id).order_by('-create_at')[:2]
        elif post_id:
            main_post = Post.objects.get(id = post_id)
            main_post.views += 1
            main_post.save()
            recommended_posts = Post.objects.exclude(id = main_post.id).filter(topic = main_post.topic).order_by('-create_at')[:2]
        else:
            main_post = None
            recommended_posts = None
    except:
        main_post = None
        recommended_posts = None

    post_id = main_post.id if main_post else None
    if request.method == "POST":
        if 'confirmDeleteBtn' in request.POST:
            if main_post:
                main_post.delete()
                return redirect('board')

    context = {
        'main_post': main_post,
        'recommended_posts': recommended_posts,
        'post_id': post_id,
    }

    return render(request, 'board.html', context)


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-views')
    serializer_class = PostSerializer

# 자동완성
def autocomplete(request):
    if request.method == "POST":

        #제목 필드값 가져옴
        prompt = request.POST.get('contentTitle')
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt},
                ],
            )
            # 반환된 응답에서 텍스트 추출해 변수에 저장
            message = response['choices'][0]['message']['content']
        except Exception as e:
            message = str(e)
        return JsonResponse({"message": message})
    return render(request, 'autocomplete.html')