from django.urls import path
from .views import home_view, login_view, add_memory_view
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('add/', add_memory_view, name='add_memory'),
    path('profile/', views.profile, name='profile'),
]