from django.shortcuts import render, redirect
from .forms import MemoryForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def profile(request):
    return render(request, 'profile.html', {
        'user': request.user
    })

def home_view(request):
    return render(request, 'home.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile')
    return render(request, 'login.html')


def add_memory_view(request):
    if request.method == 'POST':
        form = MemoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MemoryForm()

    return render(request, 'add_memory.html', {'form': form})