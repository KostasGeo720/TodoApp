from django.urls import path
from . import views

urlpatterns = [
    path('profile/new/', views.new_profile, name='new_profile'),
]
