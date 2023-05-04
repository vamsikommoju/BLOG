from django.shortcuts import render
from app1.forms import SignUpForm,postform
from app1.models import post
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,update_session_auth_hash,login,logout
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    posts = post.objects.all()
    paginator = Paginator(posts,2)
    pageno = request.GET.get('page')
    pageobj = paginator.get_page(pageno)
    context = {'pageobj':pageobj,'count':paginator.count}
    return render(request,'app1/home.html',context)


def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registration Succesfull')
    else:
        form = SignUpForm()
    return render(request,'app1/signup.html',{'form':form,'msg':'This is Signup Form'})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Your Account has been Logged Successfully')
                    return HttpResponseRedirect('/app1/dashboard')
        else:
            form = AuthenticationForm()
        return render(request,'app1/login.html',{'form':form,'msg':'Login Page'})
    else:
        return HttpResponseRedirect('/app1/dashboard')


def user_dashboard(request):
    if request.user.is_authenticated:
        return render(request,'app1/dashboard.html',{'msg':'This is Profile Page'})
    else:
        return HttpResponseRedirect('/app1/login')



def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/app1/login')

def user_post(request):
    if request.user.is_authenticated:
        form = postform()
        if request.method == 'POST':
            form =postform(request.POST)
            if form.is_valid():
                form.save()
                form =postform()
                messages.success(request,'Course Added ')    
        return render(request,'app1/post.html',{'form':form,'name':request.user.username})
    else:
        return HttpResponseRedirect('/app1/login') 



def user_change_pwd(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request,'Password changed successfully')
                return HttpResponseRedirect('/app1/profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request,'app1/changepwd.html',{'form':form})
    else:
        return HttpResponseRedirect('/app1/login')

def user_change_pwd2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request,'Password changed successfully')
                return HttpResponseRedirect('/app1/profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request,'app1/changepwd2.html',{'form':form})
    else:
        return HttpResponseRedirect('/app1/login')
