from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.
def question_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    print (Post, '11111111111111')
    return render(request, 'question/question_list.html', {'posts': posts})


def question_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'question/question_detail.html', {'post': post})

