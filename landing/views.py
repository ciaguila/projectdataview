from django.shortcuts import render, redirect

def homepage_view(request):
        return redirect('landing:home')

def home(request):
        return render(request, 'landing/home.html')