from django.shortcuts import render, redirect
from .models import boardPost
from rest_framework import viewsets
from .serializers import boardPostSerializer

# Create your views here.

def board_client(request):
    return render(request, 'board-client.html')
def board_admin(request):
    return render(request, 'board-admin.html')
def login(request):
    return render(request, 'login.html')
def write(request):
    return render(request, 'write.html')
def board(request):
    try:
        post = boardPost.objects.latest('create_date')
    except:
        post = None
    return render(request, 'board.html', {'post': post})


class boardPostViewset(viewsets.ModelViewSet):
    queryset = boardPost.objects.all()
    serializer_class = boardPostSerializer
