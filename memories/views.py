from django.shortcuts import render, redirect
from .forms import MemoryForm
from .models import Memory
from django.contrib.auth.decorators import login_required



@login_required
def profile(request):
    return render(request, 'profile.html', {
        'user': request.user
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

