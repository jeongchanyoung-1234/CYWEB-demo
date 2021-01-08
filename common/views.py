from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from common.forms import UserForm
from django.core.mail import send_mail
from random import sample
from django.contrib.auth.models import User
# Create your views here.

def signup(request):
    """
    계정 생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

# def change_password(request):
#     """
#     비밀번호 변경
#     """
#     if request.method == "POST":
#         form = ChangePasswordForm(request.POST)
#         if form.new_password == form.new_re_password:
#
#             if form.is_valid():




# def check_password(request):
#     """
#     비밀번호 매칭
#     """
#     random_number = sample(range(10), 6)
#     random_password = ''.join(random_number)
#
#     user_id = request.user.id
#     user = User.objects.get(pk=user_id)
#     user.password1 = random_password
#
#     send_mail('임시 비밀번호를 확인하세요',
#               '발급된 임시 비밀번호는 {}입니다.'.format(random_password),
#               'jcy1996@naver.com',
#               ['{}'.format(user.email)],
#               fail_silently=False)
#
#     return redirect('index')