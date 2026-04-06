from django.shortcuts import render, redirect
from .forms import MemoryForm


def home_view(request):
    return render(request, 'home.html')


def login_view(request):
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