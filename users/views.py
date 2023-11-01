from django.shortcuts import render,redirect
from users.forms import LoginForm,SignupForm
from django.contrib.auth import authenticate, login, logout
from users.models import User




def login_view(request):
    if request.user.is_authenticated:
        return redirect("/posts/feeds/")
    
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        print("forms.is_valid():", form.is_valid())
        if form.is_valid(): #폼 데이터 존재시
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            # id,pw 가 존재하는지
            user = authenticate(username=username,password=password)
            if user:
                login(request,user) #로그인 시킴
                return redirect("/posts/feeds/")
            else:
                form.add_error(None, "입력한 자격증명에 해당하는 사용자가 없습니다!")
        #유효성 검사 이후에는 cleaned_data에서 데이터를 가져와 사용
        print("form.cleaned_data:", form.cleaned_data)
        context={
            "form":form,
        }
        return render(request,"users/login.html",context)
    else:
        form = LoginForm()
        context = {"form":form}
        return render(request,"users/login.html",context)

def logout_view(request):
    logout(request)
    return redirect("/users/login/")

def signup(request):
    if request.method == "POST":
        form = SignupForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("/posts/feeds/")
        else:
            context = {"form":form}
            return render(request, "users/signup.html",context)
    else:
        form = SignupForm()
        context = {"form":form}
        return render(request, "users/signup.html",context)
