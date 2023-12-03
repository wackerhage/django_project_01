from django.urls import path
from galeria.views import index, index2, index3

urlpatterns = [
    path('', index),
    path('index2/', index2, name='index2'),
    path('index2/index3', index3, name='index3'),
]
