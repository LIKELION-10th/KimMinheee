from django.shortcuts import render,redirect, get_object_or_404

from .forms import CommentForm
from .models import Comment

# Create your views here.
def index(request):
    comment = Comment.objects.filter().order_by('-date')
    comment_form = CommentForm()
    return render(request,'index.html',{'comment':comment, 'comment_form': comment_form})

#댓글을 생성해주는 메소드
def create_comment(request):

    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False) #아직은 db에 저장하지 말고 대기!
        finished_form.save()

        comment = Comment.objects.filter().order_by('-date')
        comment_form = CommentForm()
        return redirect('/#guestbook')



#댓글 삭제해주는 메소드
def delete(request, comment_id):
    deleteComment = get_object_or_404(Comment,pk=comment_id)
    deleteComment.delete()
    return redirect('/#guestbook')

#댓글 수정해주는 메소드
def update(request, comment_id):
    updateComment = get_object_or_404(Comment,pk=comment_id)
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            updateComment.comment=form.cleaned_data["comment"]
            updateComment.save()
            return redirect('/#guestbook')

    else:
        form=CommentForm()
    return render(request,'comment_edit.html',{'form':form})