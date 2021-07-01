from django.urls import path
from . import views


app_name = 'landing'
urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('home', views.home, name="home")
]