from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Lesson, Profile, Guest
from django.contrib import auth, messages
from django.contrib.auth.models import User
from .forms import LessonForm, ProfileForm
from django.contrib.auth.hashers import check_password
from calapp.models import Graduate
from calapp.views import add_credit


def signup(request):
    if request.method == "POST":  
        if User.objects.filter(username=request.POST['username']).exists():
            messages.info(request, "이미 존재하는 아이디 입니다.")
            return render(request, 'register.html')   
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password1"])
            auth.login(request,user)
            return redirect('signup_detail')
        else:
            messages.info(request, "비밀번호가 일치하지 않습니다.")
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')

def signup_detail(request): #회원정보 기입
    if request.method == "POST":
        new_user = Profile()
        new_user.name = request.POST["name"]
        new_user.major = request.POST["major"]
        new_user.ad_year = request.POST["ad_year"]
        new_user.user = request.user
        new_user.save()
        return redirect('home')
    form = ProfileForm()
    return render(request, 'register_detail.html',{'form':form})

def login(request):
    # request == POST 라면 로그인 GET 이라면 login html 띄우기
    if (request.method == "POST"):
        
        userid = request.POST["username"]
        userpwd = request.POST["password"]
        # 유저가 있으면 user반환 없으면 None
        user = auth.authenticate(request, username=userid, password=userpwd)
        if(user is not None):  # 만약 유저가 있다면
            auth.login(request, user)
            
            return redirect('home')
        else: #로그인 에러시
            messages.info(request, "아이디 또는 비밀번호가 틀렸습니다.")
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')

def home(request): #메인 화면
    #student = request.user
    #current_user = Profile.objects.get(user = student)
    #current_user =  get_object_or_404(Profile, user=request.user)
    current_user = request.user
    user_profile = Profile.objects.get(user = current_user)
    gradu_major = user_profile.major
    gradu_ad_year = user_profile.ad_year
    gradu = Graduate.objects.get(major=gradu_major, ad_year=gradu_ad_year)

    choicemajor = Lesson.objects.filter(link = current_user, classkind='전공선택')
    needmajor   = Lesson.objects.filter(link = current_user, classkind='전공필수')
    special     = Lesson.objects.filter(link = current_user, classkind='특화교양')
    college     = Lesson.objects.filter(link = current_user, classkind='대학별교양')
    balance     = Lesson.objects.filter(link = current_user, classkind='균형교양')
    basic       = Lesson.objects.filter(link = current_user, classkind='기초교양')
    free        = Lesson.objects.filter(link = current_user, classkind='자유선택')
    

    choicemajor = add_credit(choicemajor)
    needmajor = add_credit(needmajor)
    special = add_credit(special)
    college = add_credit(college)
    balance = add_credit(balance)
    basic = add_credit(basic)
    free = add_credit(free)

    now_credits = {
        '전공선택':[choicemajor,gradu.choicemajor],
        '전공필수':[needmajor,gradu.needmajor],
        '특화교양':[special,gradu.special],
        '대학별교양':[college,gradu.college],
        '균형교양':[balance,gradu.balance],
        '기초교양':[basic,gradu.basic],
        '자유선택':[free,gradu.free]
        }


    if (request.method == "POST"):
        new_class = Lesson()
        new_class.classname = request.POST["classname"]
        new_class.classkind = request.POST["classkind"]
        new_class.classcredits = request.POST["classcredits"]
        new_class.link = request.user
        new_class.save()   
        return redirect('home')
    return render(request,'index.html',{'user':current_user,'credits':now_credits})

def delete(request, class_id):
    delete_lesson = get_object_or_404(Lesson, pk=class_id) #수강한 과목 지우기
    print(delete_lesson)
    delete_lesson.delete()
    return redirect('home')

def delete_all(request):
    delete_all_lesson = Lesson.objects.filter(link=request.user)
    delete_all_lesson.delete()
    return redirect('home')

# def class_modify(request, class_id):
#     print(class_id)
#     #modify_lesson = get_object_or_404(Lesson, pk=class_id)
#     modify_lesson = Lesson.objects.get(pk=class_id)
#     print(modify_lesson.classname)
#     if request.method == "POST":
#         if(request.POST['classname'] != ''):
#             modify_lesson.classname = request.POST['classname']
#         if(request.POST['classkind'] != ''):
#             modify_lesson.classkind = request.POST['classkind']
#         if(request.POST['classcredits'] != ''):
#             modify_lesson.classcredits = request.POST['classcredits']
#         modify_lesson.save()
#         return redirect('home')
#     return redirect('home')

    

################################################
#회원정보/비밀번호 수정 html
def modify(request):
    return render(request, 'modify.html')

#비밀번호 수정
def modify_password(request):
    if request.method == "POST":
        curr_password = request.POST.get("curr_password")
        user = request.user
        if check_password(curr_password, user.password):
            new_password = request.POST.get("new_password")
            password_confirm = request.POST.get("repeat_password")
            if new_password == password_confirm:
                user.set_password(new_password)
                user.save()
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('home')
            else:
                messages.info(request, "새로운 비밀번호를 다시 확인해주세요.")
                return render(request, 'modify.html')
        else:
            messages.info(request, "현재 비밀번호가 일치하지 않습니다.")
            return render(request, 'modify.html')
    else:
        return render(request, 'modify.html')


#회원정보 수정
def modify_userinfo(request):
    student = request.user
    Sprofile = Profile.objects.get(user = student)
    #print("학생", Sprofile.name)
    if request.method == "POST":
        if(request.POST['name'] != ''):
            Sprofile.name = request.POST['name']
        if(request.POST['major'] != ''):
            Sprofile.major = request.POST['major']
        if(request.POST['admisson_year'] != ''):
            Sprofile.ad_year = request.POST['admisson_year']
        Sprofile.save()
        return redirect('home') #메인화면으로
    return render(request, 'modify.html') #수정화면


################################################################
#
#
###비회원 로그인
#def guest_login(request):
#    if request.method == "POST":
#        guest = Guest()
#        guest.major = request.POST['major']
#        guest.ad_year = request.POST['ad_year']
#        guest.save()
#        form = LessonForm()
#        return render(request,'guest_index.html',{'guest':guest,'form':form})
#
#    return render(request, 'guest_login.html')
#
#def guest_home(request,guest_id):
#    if (request.method == "POST"):
#        guest = get_object_or_404(Guest,pk=guest_id)
#        form = LessonForm()   
#        filled_form = LessonForm(request.POST)
#        if (filled_form.is_valid()):
#            finished_form = filled_form.save(commit=False)
#            finished_form.guest_link = get_object_or_404(Guest,pk=guest_id)
#            finished_form.save()
#            return render(request,'guest_index.html',{'guest':guest,'form':form})
#
#def guest_delete(request,class_id):
#    delete_post = get_object_or_404(Lesson, pk=class_id) #수강한 과목 지우기
#    delete_post.delete()
#    return redirect('geust_home',)