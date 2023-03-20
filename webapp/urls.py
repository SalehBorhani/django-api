from django.urls import path
from webapp.views import *

app_name = 'webapp'

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('elements', elements, name='elements')
 
]
