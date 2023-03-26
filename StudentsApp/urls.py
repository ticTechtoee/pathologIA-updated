from django.urls import path
from . import views

app_name = 'StudentsApp'

urlpatterns = [
    path('GetQuestionnaireList/', views.ViewGetQuestionnaireList, name='GetQuestionnaireListView'),
    path('GetQuestionList/<str:pk>', views.ViewGetQuestionsList, name='GetQuestionsListView'),
    path('Result/', views.ViewResult, name='ResultView'),

    ]
