from django.urls import path
from . import views

app_name = 'DemarcateApp'

urlpatterns = [
    path('SelectImage/', views.ViewSelectImage, name='SelectImageView'),
    path('CreateQuestion/<str:pk>', views.ViewCreateDemarcateQuestion, name='CreateDemarcateQuestionView'),
]
