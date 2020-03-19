from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.

def customer(request):
    return render(request, 'customer.html', {'name': 'Srijeet'})

# def add(request):
#     a = int(request.POST['num1'])
#     b = int(request.POST['num2'])
#     sum = a + b
#     return render(request, 'result.html', {'result': sum})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log the user in
            login(request, user)
            return redirect("index.html")

    else:
        form =UserCreationForm()
    
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            #log in the user
            user = form.get_user()
            login(request, user)
            return redirect("index.html")
    else: 
        form =AuthenticationForm()
    
    return render(request, 'login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect("index.html")

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login_new(request):
    return render(request, 'login.html')

def wedding(request):
    return render(request, 'wedding.html')

def birthday(request):
    return render(request, 'birthday.html')

def anniversary(request):
    return render(request, 'anniversary.html')

def corporate(request):
    return render(request, 'corporate.html')

def cultural(request):
    return render(request, 'cultural.html')

def customize(request):
    return render(request, 'customize.html')

def submit_details(request):
    return render(request, 'submit_details.html')

