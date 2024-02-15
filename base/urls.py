from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms_page/<str:pk>/', views.rooms, name='room'),
]