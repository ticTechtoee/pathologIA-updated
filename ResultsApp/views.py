from collections import defaultdict
from django.shortcuts import render
from StudentsApp.models import StudentPerformance
from .forms import StudentSearchForm
from django.db.models import Sum

from collections import defaultdict

from decimal import Decimal, getcontext

def ViewStudentResults(request):
    student_performances = StudentPerformance.objects.filter(Student_Information=request.user)
    
    # Group by 'Question_Group_Information' and annotate with the sum of scores for each group
    grouped_results = student_performances.values('Question_Group_Information__Name_Of_Group').annotate(total_score=Sum('Score_Per_Question'))

    total_score = Decimal(0.00)

    for group in grouped_results:
        score_per_group = Decimal(group['total_score'])
        total_score += score_per_group

    print(total_score)
    context = {'Group_Information': grouped_results, 'Total_Score': total_score}
    return render(request, 'index.html', context)


def ViewSearchStudentPerformance(request):
    form = StudentSearchForm(request.GET)
    results = []

    if form.is_valid():
        username = form.cleaned_data['username']
        results = StudentPerformance.objects.filter(Student_Information__username=username)

    return render(request, 'search_student_performance.html', {'form': form, 'results': results})