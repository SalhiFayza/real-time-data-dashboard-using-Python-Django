from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm
from django.shortcuts import render
import pyrebase
import json
import logging

Config = {
  'apiKey': "AIzaSyBltP6KvGHIwVhbGrPO0J0CZNCKowsgfwc",
  'authDomain': "aquaponicsapp-d4dda.firebaseapp.com",
  'databaseURL': "https://aquaponicsapp-d4dda-default-rtdb.firebaseio.com",
  'projectId': "aquaponicsapp-d4dda",
  'storageBucket': "aquaponicsapp-d4dda.appspot.com",
  'messagingSenderId': "512029563756",
  'appId': "1:512029563756:web:080bf8207231db6c86b149",
  'measurementId': "G-LVBS1V1NLS"
};


firebase=pyrebase.initialize_app(Config)
authe = firebase.auth()
database=firebase.database() 
logger = logging.getLogger(__name__)

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            if(username=="aquaponicssfax@entcom.tn"):
             try:
              logger.error('firebase')
        # creating a user with the given email and password
              user=authe.sign_in_with_email_and_password(username,password)
             except:
                msg = 'Error validating the form' 
                return render(request, "accounts/login.html", {"form": form, "msg" : msg})
             session_id=user['idToken']
             request.session['uid']=str(session_id)
             return redirect("/")
            else:
                logger.error('local')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("/")
                else:    
                     msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "accounts/login.html", {"form": form, "msg" : msg})

def register_user(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg     = 'User created - please <a href="/login">login</a>.'
            success = True
            
            #return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })
