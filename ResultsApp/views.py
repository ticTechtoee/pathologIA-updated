from django.shortcuts import render
from StudentsApp.models import StudentPerformance, StudentPerfomranceInDemarcateQuizes
from .forms import StudentSearchForm
from django.db.models import Sum, F, DecimalField

def ViewStudentResults(request):
    student_performances = StudentPerformance.objects.filter(Student_Information=request.user)
    student_performances_D = StudentPerfomranceInDemarcateQuizes.objects.filter(Student_Information=request.user)

    # Annotate the total score for regular performances
    grouped_results = student_performances.values('Question_Group_Information__Name_Of_Group').annotate(
        total_score=Sum(F('Score_Per_Question'), output_field=DecimalField())
    )

    # Annotate the total score for demarcate performances
    demarcate_grouped_results = student_performances_D.values('Question_Group_Information__Name_Of_Group').annotate(
        total_score=Sum(F('Score_Per_Question'), output_field=DecimalField())
    )

    # Calculate the total scores for regular and demarcate performances
    total_score = sum(group['total_score'] for group in grouped_results)
    D_total_score = sum(D_group['total_score'] for D_group in demarcate_grouped_results)

    context = {
        'Group_Information': grouped_results,
        'Total_Score': total_score,
        'Group_Information_Demarcate': demarcate_grouped_results,
        'Total_D_Score': D_total_score
    }
    return render(request, 'index.html', context)



def ViewSearchStudentPerformance(request):
    form = StudentSearchForm(request.GET)
    grouped_results = None
    total_score = None 
    demarcate_grouped_results = None
    D_total_score = None
    if request.method == 'POST':
 
        username = request.POST.get('username')
        
        student_performances = StudentPerformance.objects.filter(Student_Information__username=username)
        student_performances_D = StudentPerfomranceInDemarcateQuizes.objects.filter(Student_Information__username=username)

        # Annotate the total score for regular performances
        grouped_results = student_performances.values('Question_Group_Information__Name_Of_Group').annotate(
            total_score=Sum(F('Score_Per_Question'), output_field=DecimalField())
        )

        # Annotate the total score for demarcate performances
        demarcate_grouped_results = student_performances_D.values('Question_Group_Information__Name_Of_Group').annotate(
            total_score=Sum(F('Score_Per_Question'), output_field=DecimalField())
        )

        # Calculate the total scores for regular and demarcate performances
        total_score = sum(group['total_score'] for group in grouped_results)
        D_total_score = sum(D_group['total_score'] for D_group in demarcate_grouped_results)
    context = {
        'form': form,
        'Group_Information': grouped_results,
        'Total_Score': total_score,
        'Group_Information_Demarcate': demarcate_grouped_results,
        'Total_D_Score': D_total_score
        }

    return render(request, 'search_student_performance.html', context)