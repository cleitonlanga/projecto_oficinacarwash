from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import Pessoa,User

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       nome = request.POST.get('nome')
       sobrenome = request.POST.get('sobrenome')
       profissao = request.POST.get('profissao')
       birthday = request.POST.get('birthday')
       nationality = request.POST.get('nationality')
       province = request.POST.get('province')
       bi = request.POST.get('bi')
       city = request.POST.get('city')
       contact = request.POST.get('contact')
       
       cliente = Pessoa.objects.filter(bi=bi)
       
       user = User.objects.create_user(username=username, password=password)
       pessoa = Pessoa.objects.all()
       
       
       
       return redirect('signin')
    else:
        return render(request, 'signup.html')
    
       
       


def sigin_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, User)
            return redirect('atualiza_cliente')
        else:
            return render(request, 'signin.html',{'error':'password ou username incorrectos'})
    else:
        return render(request, 'signin.html')
        
    
    