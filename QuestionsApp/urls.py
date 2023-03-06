from django.urls import path
from . import views

app_name = 'QuestionsApp'

urlpatterns = [
    path('CreateQuestionGroup/', views.ViewCreateQuestionGroup, name='CreateQuestionGroupView'),
    path('CreateQuestion/', views.ViewCreateQuestion, name='CreateQuestionView'),
    path('CreateOption/', views.ViewCreateOption, name='CreateOptionView'),

]
