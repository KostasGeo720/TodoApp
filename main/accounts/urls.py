from django.urls import path
from . import views

urlpatterns = [
    path('profile/new/', views.new_profile, name='new_profile'),
    path('login/', views.login, name='login'),
]
