from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(label='이메일')

    class Meta:
        model = User
        fields = ('username', 'email')
#
# class ChangePasswordForm(forms.Form):
#     password = forms.PasswordInput(label='원래 비밀번호')
#     new_password = forms.PasswordInput(label='새 비밀번호')
#     new_re_password = forms.PasswordInput(label='새 비밀번호 확인')
#     user = User.objects.get(pk=)
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         new_password = cleaned_data.get('new_password')
#         new_re_password = cleaned_data.get('new_re_password')
#         if password != request.user.password
