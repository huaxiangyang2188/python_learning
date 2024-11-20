from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
'''
def login_view(request):
    """用户登录"""
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
'''

def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse("learning_logs:index"))
def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 显示空注册表单
        form = UserCreationForm()
    else:
        """处理表单数据"""
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录，再重定向到首页
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse("learning_logs:index"))
    context = {'form': form}
    return render(request,'users/register.html', context)