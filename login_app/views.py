from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print("user: ", user.id)
        user_id = user.id
        print("user_id: ", user_id)
        login_time = time.time()

        if user is not None:
            login(request, user)
            return redirect('login:home')
        else:
            messages.info(request, 'Username or Password incorrect')
            return render(request, "index.html", )
    context = {}
    return render(request, "login.html", context)