from django.urls import path
from . import views

app_name = 'DemarcateApp'

urlpatterns = [
    path('CreateQuestion/', views.ViewCreateDemarcateQuestion, name='CreateDemarcateQuestionView'),
]
