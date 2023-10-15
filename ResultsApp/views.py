from django.shortcuts import render
from StudentsApp.models import StudentPerformance
from .forms import StudentSearchForm
from django.db.models import Sum

def ViewStudentResults(request):
    student = request.user
    results = (
        StudentPerformance.objects
        .filter(Student_Information=student)
        .values('Question_Group_Information', 'Completed_At')
        .annotate(total_score=Sum('Score_Per_Question'))
        .order_by('Question_Group_Information'))
    print(results)

    return render(request, 'index.html', {'results': results})

def ViewSearchStudentPerformance(request):
    form = StudentSearchForm(request.GET)
    results = []

    if form.is_valid():
        username = form.cleaned_data['username']
        results = StudentPerformance.objects.filter(Student_Information__username=username)

    return render(request, 'search_student_performance.html', {'form': form, 'results': results})