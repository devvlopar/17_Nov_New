
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('ashwini/', fun1, name="ashwini"),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('register/', register, name='shweta'),
    path('login/', login, name='login'),
    path('otp/', otp, name='otp'),
    path('contact/', contact, name='contact'),



]