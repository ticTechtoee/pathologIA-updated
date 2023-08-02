from django.urls import path
from . import views

app_name = 'ResultsApp'

urlpatterns = [
    path('', views.ViewStudentResults, name='StudentsResultsView'),
    path('SearchResult', views.ViewSearchStudentPerformance, name='SearchStudentPerformanceView'),
]
