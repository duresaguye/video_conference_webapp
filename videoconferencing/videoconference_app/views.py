from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import Room
from django.utils.text import slugify
from django.views.decorators.cache import never_cache

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/?success=Registration successful. Please login.')
        else:
            error_message = form.errors.as_text()
            return render(request, 'register.html', {'form': form, 'error_message': error_message})
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard/')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
 
    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect('/login/')

@login_required
@never_cache
def dashboard(request):
    return render(request, 'dashboard.html', {'name': request.user.username}) 


@login_required
@never_cache
def chat_room(request, room_name):
    return render(request, 'chat_room.html', {
        'room_name': room_name,
        'username': request.user.username,
    })
@login_required
@never_cache
def video_call(request):
    return render(request, 'video_call.html')

