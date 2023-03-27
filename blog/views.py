from django.shortcuts import render


# Create your views here.

def blog_view(request):
    return render(request, 'blog/blog-home.html')

def blog_single(request):
    context = {'title': 'Saleh has won the gold medal of the WorldSkills 2026 in CloudComputing!'}
    return render(request, 'blog/blog-single.html', context=context)