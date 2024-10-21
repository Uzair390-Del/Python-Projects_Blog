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
#from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

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
def search(request):
    query = request.GET.get('q')
    if query:
        results = Post.objects.filter(title__icontains=query)  # Adjust the filter to match your model
    else:
        results = Post.objects.none()
    return render(request, 'blog/search_results.html', {'results': results, 'query': query})
def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Here you can add logic to store the email in a database, send a confirmation email, etc.
        
        # Example: Sending a confirmation email (optional)
        send_mail(
            'Subscription Confirmation',
            'Thank you for subscribing to the Energy Efficient AI Blog!',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
        
        # Redirect to a "thank you" page or back to the home page
        return redirect('home')

    # If someone visits /subscribe/ directly (not through POST form), you could redirect them:
    return redirect('home')

# # Home view
# def home(request):
#     return render(request, 'blog/test.html')


# Create your views here.
