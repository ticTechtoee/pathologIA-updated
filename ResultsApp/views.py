from django.shortcuts import render
from StudentsApp.models import StudentPerformance
from .forms import StudentSearchForm


def ViewStudentResults(request):
    # Retrieve the student's results sorted by Question_Group_Information
    student = request.user  # Assuming you are using Django's authentication system
    results = StudentPerformance.objects.filter(Student_Information=student).order_by('Question_Group_Information')
    
    return render(request, 'index.html', {'results': results})

def ViewSearchStudentPerformance(request):
    form = StudentSearchForm(request.GET)
    results = []

    if form.is_valid():
        username = form.cleaned_data['username']
        results = StudentPerformance.objects.filter(Student_Information__username=username)

    return render(request, 'search_student_performance.html', {'form': form, 'results': results})