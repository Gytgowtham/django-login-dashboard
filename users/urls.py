from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),      # http://127.0.0.1:8000/
    path('dashboard/', views.dashboard, name='dashboard'),
]
