from django.shortcuts import render
from StudentsApp.models import StudentPerformance


def ViewStudentResults(request):
    # Retrieve the student's results sorted by Question_Group_Information
    student = request.user  # Assuming you are using Django's authentication system
    results = StudentPerformance.objects.filter(Student_Information=student).order_by('Question_Group_Information')
    
    return render(request, 'index.html', {'results': results})
