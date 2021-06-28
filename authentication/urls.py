

from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView

from django.contrib import admin
from django.urls import path
urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path('admin/', admin.site.urls),
    
]
