from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Comment
from django.contrib import auth
from django.contrib.auth.models import User
from .forms import CommentForm, ProfileForm


def signup(request):
    if request.method == "POST":  
        if User.objects.filter(username=request.POST['username']).exists():
            flag = 1 #아이디 중복 체크 username이 이미 존재하면 flag 리턴
            return render(request, 'register.html',{'flag':flag})   
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password1"])
            auth.login(request,user)
            return redirect('signup_detail')
        else:
            flag = 1 #비밀번호 비밀번화 확인이 다를때
            return render(request, 'register.html',{'other_flag':flag})
    else:
        return render(request, 'register.html')

def signup_detail(request): #회원정보 기입
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.user = request.user
            unfinished.save()
            return redirect('home')
    form = ProfileForm()
    return render(request, 'register_detail.html',{'form':form})

def login(request):
    # request == POST 라면 로그인 GET 이라면 login html 띄우기
    if (request.method == "POST"):
        
        userid = request.POST["username"]
        userpwd = request.POST["password1"]
        # 유저가 있으면 user반환 없으면 None
        user = auth.authenticate(request, username=userid, password=userpwd)
        if(user is not None):  # 만약 유저가 있다면
            auth.login(request, user)
            
            return redirect('home')
        else: #로그인 에러시
            flag = 1
            return render(request, 'login.html',{'flag':flag})

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')

def home(request): #메인 화면
    form = CommentForm()
    current_user = request.user
    if (request.method == "POST"):   
        filled_form = CommentForm(request.POST)
        if (filled_form.is_valid()):
            finished_form = filled_form.save(commit=False)
            finished_form.link = request.user #수강한 과목 객체와 유저객체와 연결
            finished_form.save()
            return redirect('home')
    return render(request,'index.html',{'form':form,'user':current_user})

def delete(request,comment_id):
    delete_post = get_object_or_404(Comment, pk=comment_id) #수강한 과목 지우기
    delete_post.delete()
    return redirect('home')
