from django.shortcuts import render,redirect
from posts.models import Post

def feeds(request):
    
    if not request.user.is_authenticated: #요청한 유자가 인증되지 않은경우
        return redirect("/users/login/")
    
    posts= Post.objects.all()
    context={"posts":posts}
        
    return render(request,"posts/feeds.html",context)

