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
    memories = Memory.objects.all().order_by('-created_at')  # получаем воспоминания
    return render(request, 'home.html', {
        'memories': memories
    })


def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile')
    return render(request, 'login.html')


def add_memory(request):
    if request.method == 'POST':
        form = MemoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MemoryForm()

    return render(request, 'add_memory.html', {'form': form})
