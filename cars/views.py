from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Car
from .forms import CarForm, RegisterForm, LoginForm
# Create your views here.

def is_admin(user):
    return user.is_superuser

def main_page(request):
    print(request.user)
    return render(request, 'main_page.html', {'cars':Car.objects.all()})

@user_passes_test(is_admin, login_url='/adminlogin/')
def admin_page(request):
    return render(request, 'admin_page_main.html', {'cars':Car.objects.all()})

@user_passes_test(is_admin, login_url='/adminlogin/')
def list_of_users(request):
    return render(request, 'admin_page_users.html', {'acounts':User.objects.all()})

@user_passes_test(is_admin, login_url='/adminlogin/')
@csrf_exempt
def add(request):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('/myadmin/')
            # return render(request, 'admin_page_main.html', {'cars': Car.objects.all()})
    else:
        form = CarForm()
    return render(request, 'admin_page_add.html', {'form': form})

@user_passes_test(is_admin, login_url='/adminlogin/')
@csrf_exempt
def car_detail(request, id):
    car = get_object_or_404(Car, id=id)
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            post = form.save()
            return redirect('/myadmin/')
            # return render(request, 'admin_page_main.html', {'cars': Car.objects.all()})
    else:
        form = CarForm(instance=car)
    return render(request,'car_detail.html', {'form': form, 'car':car})

@user_passes_test(is_admin, login_url='/adminlogin/')
def car_delete(request, id):
    car = Car.objects.get(id=id)
    car.delete()
    return redirect('/myadmin/')

@user_passes_test(is_admin, login_url='/adminlogin/')
def orders(request):
    pass

@csrf_exempt
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('/')
            # return render(request, 'admin_page_main.html', {'cars': Car.objects.all()})
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


@csrf_exempt
def login_user(request):
    if request.method=="POST":
            username = request.POST['username']
            password = request.POST['password']
            print(username)
            print(password)
            try:
                user = User.objects.get(username=username, password=password)
            except Exception:
                return render(request, 'login.html', {'form': LoginForm()})
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
            # Redirect to a success page.
                    return redirect('/')
                else:
                    print('bad')
                    form = LoginForm()
            # Return a 'disabled account' error message
            else:
                print('badbad')
                form = LoginForm()
        # Return an 'invalid login' error message.
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@csrf_exempt
def admin_login(request):
    if request.method=="POST":
            username = request.POST['username']
            password = request.POST['password']
            print(username)
            print(password)
            try:
                user = User.objects.get(username=username) # password=password - тоже надо учесть
            except Exception:
                return render(request, 'login.html', {'form': LoginForm()})
            print(user)
            if user is not None and user.is_superuser:
                if user.is_active:
                    login(request, user)
            # Redirect to a success page.
                    return redirect('/myadmin/')
                else:
                    print('bad')
                    form = LoginForm()
            # Return a 'disabled account' error message
            else:
                print('badbad')
                form = LoginForm()
        # Return an 'invalid login' error message.
    else:
        form = LoginForm()
    return render(request, 'admin_login.html', {'form': form})

@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return redirect('/')


@csrf_exempt
def search(request):
    pass

@login_required(login_url='/login/')
def order(request):
    pass