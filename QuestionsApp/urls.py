from django.urls import path
from . import views

app_name = 'QuestionsApp'

urlpatterns = [
    path('CreateQuestionGroup/', views.ViewCreateQuestionGroup, name='CreateQuestionGroupView'),
    path('CreateQuestionGroup/<str:pk>/', views.ViewEditQuestionGroup, name='EditQuestionGroupView'),
    path('DeleteQuestionGroup/<str:pk>/', views.ViewDeleteQuestionGroup, name='DeleteQuestionGroupView'),
    path('CreateQuestion/', views.ViewCreateQuestion, name='CreateQuestionView'),
    path('CreateOption/', views.ViewCreateOption, name='CreateOptionView'),

]
