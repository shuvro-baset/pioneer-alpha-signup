from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('', home, name='home'),
    path('login', login, name='login')

]