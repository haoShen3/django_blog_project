from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
from .forms import CommentForm
from blog.models import Post
# Create your views here.


def post_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            comment_list = Comment.objects.all()
            context = {'post': post,
                       'form':form,
                       'comment_list': comment_list}
            return render(request, 'blog/detail.html', context=context)
