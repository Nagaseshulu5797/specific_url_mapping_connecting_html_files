

from django.urls import path

from app1.views import *

app_name='seshu'

urlpatterns=[
    path('app1_first/',app1_first,name='app1_first'),
]
