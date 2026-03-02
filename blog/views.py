from django.shortcuts import render , get_object_or_404 , redirect
from .models import Post , Feedback
from .forms import FeedbackForm

def home(request):
    posts = Post.objects.filter(is_active=True).order_by('-created_at')
    context = {
        'posts': posts
    }
    return render(request,'home.html',context)

def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    context = {
        'post': post
    }
    return render(request,'post_detail.html',context)


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['feedback_success'] = True
            return redirect('thank_you')
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})



def thank_you(request):

    success = request.session.pop('feedback_success')

    if not success:
        return redirect('home')

    return render(request, 'thanks.html')