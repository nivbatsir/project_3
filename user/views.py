from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm,CustomUserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages

# Create your views here.

def username_not_unique(username):
    if User.objects.filter(username=username):
        return True
    return False 

def email_not_unique(email):
    if User.objects.filter(email=email):
        return True
    return False

def main(request):
    return render(request,'user/main.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('show-categories')
    if request.method == "POST":
        is_staff = request.POST.get('is_staff') == 'on'
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid():
            if username_not_unique(form.cleaned_data['username']):
                messages.error(request,f"A user with that username already exists - {form.cleaned_data['username']}")
                return redirect('signup')
            if email_not_unique(form.cleaned_data['email']):
                messages.error(request,f"A user with that email already exists - {form.cleaned_data['email']} ")
                return redirect('signup')
            
            new_user = User(
               username = form.cleaned_data['username'],
               password = make_password(form.cleaned_data['password']),
               first_name = form.cleaned_data['first_name'],
               last_name = form.cleaned_data['last_name'],
               email = form.cleaned_data['email'],
               is_staff = is_staff 
            )
            
            new_user.save()
            messages.success(request,f"User succesfully created - {form.cleaned_data['username']}") 
            return redirect('login')
    else:
        form = CustomUserCreationForm()  
    return render(request,'user/signup.html',{"form":form})



def login_user(request):
    if request.user.is_authenticated:
        return redirect('show-categories')
    if request.method == "POST":
            form = CustomUserLoginForm(request.POST) 
            if form.is_valid():
                user = authenticate(request,
                                    username=request.POST['username'],
                                    password=request.POST['password']
                                    )
                if user is not None:
                    login(request,user)
                    return redirect('new-cart')
                else:
                    messages.error(request,"Wrong username or password")
                    return redirect('login')
    else: 
        form = CustomUserLoginForm()
    return render(request,'user/login.html',{"form":form})



def logout_user(request):
    logout(request)
    return redirect('main-page')


@login_required(login_url="login")
def edit_user(request):
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        is_staff = request.POST.get('is_staff') == 'on'
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid():
            if username_not_unique(form.cleaned_data['username']) and form.cleaned_data['username'] != request.user.username:
                messages.error(request,f"A user with that username already exists - {form.cleaned_data['username']}")
                return redirect('change-user-details')
            if email_not_unique(form.cleaned_data['email']) and form.cleaned_data['email'] != request.user.email:
                messages.error(request,f"A user with that email already exists - {form.cleaned_data['email']} ")
                return redirect('change-user-details')
            
            user.username = form.cleaned_data['username']
            user.password = make_password(form.cleaned_data['password'])
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.is_staff = is_staff 
            
            user.save()
            messages.success(request,f"User details succesfully changed - {form.cleaned_data['username']}") 
            return redirect('user-info')
    else:
        form = CustomUserCreationForm()  
    return render(request,'user/edit_user.html',{"form":form,"user":user})


@login_required(login_url="login")
def show_user(request):
    user = User.objects.get(id=request.user.id)
    return render(request,'user/user_info.html',{"user":user})



def login_manager(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('show-deliveries-not-deliver-yet')
    
    if request.method == "POST":
            form = CustomUserLoginForm(request.POST) 
            if form.is_valid():
                user = authenticate(request,
                                    username=request.POST['username'],
                                    password=request.POST['password']
                                    )
                if user is not None and user.is_staff:
                    login(request,user)
                    return redirect('show-deliveries-not-deliver-yet')
                elif user is not None and not user.is_staff:
                    messages.error(request,"You are not manager, go to login page!")
                    return redirect('login-manager')
                else:
                    messages.error(request,"Wrong username or password")
                    return redirect('login-manager')
    else: 
        form = CustomUserLoginForm()
    return render(request,'user/login_manager.html',{"form":form})