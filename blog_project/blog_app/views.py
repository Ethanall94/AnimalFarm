from django.shortcuts import render, redirect

# Create your views here.

def board_cilent(request):
    return render(request, 'blog_app/board-cilent.html')
def board_admin(request):
    return render(request, 'blog_app/board-admin.html')
def login(request):
    return render(request, 'blog_app/login.html')
def write(request):
    return render(request, 'blog_app/write.html')
def board(request):
    return render(request, 'blog_app/board.html')