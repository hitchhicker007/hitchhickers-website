from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Author, Comment, Contactus
from marketing.models import Signup

def postlist(request):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
   

    if request.method == "POST":
        email = request.POST['email']
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {
        'object_list' : featured,
        'latest' : latest,
    }

    return render(request,'bloglist.html',context)

def post(request, id):
    post = get_object_or_404(Post, id=id)
    latest = Post.objects.order_by('-timestamp')[0:3]

    if request.method == "POST":
        try:
            comment_name = request.POST['comment-name']
            comment_email = request.POST['comment-email']
            comment_text = request.POST['comment-text']
            comm = Comment(name=comment_name, email=comment_email, comment_text=comment_text, post=post)
            comm.save()
        except:
            email = request.POST['email']
            new_signup = Signup()
            new_signup.email = email
            new_signup.save()
    
    

    context = {
        'post':post,
        'latest' : latest,
    }
    return render(request,'single.html',context)


def index(request):
    latest = Post.objects.order_by('-timestamp')[0:3]
    
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['Email']
        subject = request.POST['Subject']
        text = request.POST['comment']

        obj = Contactus(name=name, email=email, subject=subject, text=text)
        obj.save()

    context = {
        'latest' : latest,
    }
    return render(request,'index.html',context)