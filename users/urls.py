from django.urls import path
from . import views

urlpatterns = [
        path('create-account/',views.CreateAccount, name='create-account'),
        path('', views.Home, name='home'),
]
