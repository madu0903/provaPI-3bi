from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from .forms import LoginForm, UserForm
# Create your views here.

def login_view(request):
    if request.method =='POST':
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            print('Valid Login')
            user = authenticate(username=login_form.cleaned_data['username'],password=login_form.cleaned_data['password'])
            print(user)
            if user is not None:
                login(request,user)
                return redirect('index')
    else:
        login_form=LoginForm()
    context={'login_form':login_form}
    return render(request,'users/login.html',context)

def create_view(request):
    if request.method=='POST':
        create_form=UserForm(request.POST)
        if create_form.is_valid():
            user=create_form.save()
            user.is_active=True
            user.is_staff=True
            user.save()
            return redirect('login_view')

    else:
        create_form=UserForm()

    context={'create_form':create_form}
    return render(request,'users/create.html',context)

def logout_view(request):
    logout(request)
    return redirect('login_view')
