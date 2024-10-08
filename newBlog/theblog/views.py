# from django.shortcuts import render, get_object_or_404
# from .models import Post

# def home(request):
#     posts = Post.objects.all().order_by('-created_at')
#     return render(request, 'blog/home.html', {'posts': posts})

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})
from django.shortcuts import render,get_object_or_404
from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-created_at')  # Latest posts first
    return render(request, 'blog/home.html', {'posts': posts})
    # return render(request, 'blog/home.html')


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})
    # return render(request, 'blog/post_detail.html')
def about(request):
    return render(request, 'blog/about.html')

# # Home view
# def home(request):
#     return render(request, 'blog/test.html')


# Create your views here.
