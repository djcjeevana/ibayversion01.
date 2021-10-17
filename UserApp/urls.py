from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView
from .forms import  UserLoginForm


from .views import *

app_name = 'account'

urlpatterns = [
  path('login/', login_view, name='login'),
  path('logout/', logout_view, name='logout'),
  path('register/', account_register, name='register'),
  path('activate/<slug:uidb64>/<slug:token>)/',account_activate, name='activate'),
  path('dashboard/', dashboard, name='dashboard'),
  path('account/', account_view, name='account'),
  path('profile/', userprofile, name='userprofile'),
  
   
] 







