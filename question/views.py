from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
def question_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    print (Post, '11111111111111')
    return render(request, 'question/question_list.html', {'posts': posts})


def question_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'question/question_detail.html', {'post': post})


# def question_new(request):
#     form = PostForm()
#     return render(request, 'question/question_edit.html', {'form': form})

def question_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('question_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'question/question_edit.html', {'form': form})

def question_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('question_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'question/question_edit.html', {'form': form})

