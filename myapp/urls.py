
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('ashwini/', fun1, name="ashwini"),
    path('', index, name='index'),
    path('about/', about, name='about')
]