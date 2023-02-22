from django.urls import path
from . import views

app_name = 'ImagesApp'

urlpatterns = [
    path('Index/', views.ViewIndex, name='IndexView'),
]
