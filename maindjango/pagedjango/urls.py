from django.urls import path
from .views import Home
from pagedjango.views import *


app_name='pagedjango'

urlpatterns=[
    path('', Home.as_view(), name="pagedjango"),
    
]