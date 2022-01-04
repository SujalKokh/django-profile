from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('sketch/', get),
    path('create-sketch/', create)
]
