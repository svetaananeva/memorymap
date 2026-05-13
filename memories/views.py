from django.shortcuts import render, redirect
from .forms import MemoryForm
from .models import Memory
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User



@login_required
def profile(request):
    return render(request, 'profile.html', {
        'user': request.user,
        'email': request.user.email
    })


def home_view(request):
    if request.user.is_authenticated:
        memories = Memory.objects.filter(user=request.user).order_by('-created_at')
    else:
        memories = []

    return render(request, 'home.html', {
        'memories': memories
    })


def login_view(request):

    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        from django.contrib.auth.models import User

        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username
        except User.DoesNotExist:
            username = None

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')

@login_required
def add_memory_view(request):
    if request.method == 'POST':
        form = MemoryForm(request.POST, request.FILES)

        if form.is_valid():
            memory = form.save(commit=False)
            memory.user = request.user
            memory.save()
            return redirect('home')

        print(form.errors)

    else:
        form = MemoryForm()

    return render(request, 'add_memory.html', {'form': form})


def signup_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request, 'signup.html')