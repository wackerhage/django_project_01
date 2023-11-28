from django.urls import path
from galeria.views import index, index2

urlpatterns = [
    path('', index),
    path('index2/', index2, name='index2'),
]
