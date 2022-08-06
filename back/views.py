from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .models import Student, Guest


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
    student = Student.objects.filter(author=request.user).first()
    # print("학생", student.name)
    if request.method == "POST":
        if(request.POST['name'] != ''):
            student.name = request.POST['name']
        if(request.POST['major'] != ''):
            student.major = request.POST['major']
        if(request.POST['admisson_year'] != ''):
            student.admisson_year = request.POST['admisson_year']
        student.save()
        return redirect('home') #메인화면으로
    return render(request, 'modify.html') #수정화면


################################################################


#비회원 로그인
def guest_login(request):
    if request.method == "POST":
        guest = Guest()
        guest.major = request.POST['major']
        guest.admisson_year = request.POST['admisson_year']
        guest.save()
        return redirect('home')

    return render(request, 'guest_login.html')