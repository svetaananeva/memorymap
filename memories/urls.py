from django.urls import path
from .views import home_view, login_view, add_memory_view

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('add/', add_memory_view, name='add_memory'),
]