from django.shortcuts import render, redirect
from .forms import PostForm

# Create your views here.

def board_cilent(request):
    return render(request, 'blog_app/board-cilent.html')
def board_admin(request):
    return render(request, 'blog_app/board-admin.html')
def login(request):
    return render(request, 'blog_app/login.html')
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
    return render(request, 'blog_app/write.html', context)
def board(request):
    return render(request, 'blog_app/board.html')