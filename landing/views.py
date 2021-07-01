from django.shortcuts import render, redirect

def homepage_view(request):
        return redirect('landing:home')

def home(request):
        current_user = request.user
        user_id = current_user.id
        context = {'user_id' : user_id}
        return render(request, 'landing/home.html', context)