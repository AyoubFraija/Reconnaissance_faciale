from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from scan import scanner
from train import train_fct
from detection import detecter
from pages.models import Presence
from django.utils import timezone

# Create your views here.
def login_page(request):
    return render(request, "login.html")

def seconnecter(request):
    if request.method=="POST":
        nom=request.POST['nom']
        mdp=request.POST['mdp']
        user=authenticate(username=nom,password=mdp)
        if user is not None:
            login(request,user)
            presence=Presence(username=nom,date=user.last_login)
            presence.save()
            request.session['username'] = nom
            return redirect('detection_page')
        else :
            return redirect('login_page')
        
def home(request,username):
    presences = Presence.objects.filter(username__in=['', username])
    return render(request, "home.html",{'presences': presences})

def inscription(request):
    if request.method=="POST":
        nom=request.POST['nom']
        mdp=request.POST['mdp']
        user=User.objects.create_user(username=nom,password=mdp)
        user.save()
        request.session['user_id'] = user.id
        return redirect('inscription_2')

def inscription_2(request):
    return render(request, "scan.html")

def inscription_1(request):
    return render(request, "inscription_1.html")

def scan(request):
    user_id = request.session.get('user_id')
    if user_id is not None:
        scanner(user_id)  
        return redirect('train')
    
def train(request):
    train_fct()
    return redirect('login_page')

def detection_page(request):
    return render(request, "detection.html")

def detection(request):
    names=["","","","","","",""]
    detected = False
    for u in User.objects.raw('SELECT * FROM auth_user'):
        names.append(u.username)
    detected,username = detecter(names, request.session.get('username'))
    if detected:
        presence = Presence.objects.filter(username=username).latest('id')
        presence.present = "Présent"
        presence.save()
        return redirect('home', username)
    
def deconnecter(request):
    if 'username' in request.session:
        del request.session['username']
    logout(request)
    return redirect('login_page')