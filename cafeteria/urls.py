from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('menu/', views.secret_menu, name='secret_menu'),
]
