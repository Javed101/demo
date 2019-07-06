from django.urls import path
from core import views as vs

urlpatterns = [
    path('', vs.index),
]

