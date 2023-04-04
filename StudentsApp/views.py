from django.shortcuts import render, redirect
from QuestionsApp.models import QuestionsModel, QuestionGroupModel,MCQModel
from StudentsApp.models import StudentPerformance
from AccountsApp.models import CustomUserModel
from .forms import GetQuestionnaireListForm
from django.urls import reverse
from django.http import HttpResponse, HttpResponseBadRequest


def ViewGetQuestionnaireList(request):
    form = GetQuestionnaireListForm()
    if request.method == 'POST':
        get_questionnaire_id = request.POST.get('Name_Of_Group')
        return redirect(reverse('StudentsApp:GetQuestionsListView', kwargs = {'pk':str(get_questionnaire_id)}))
    context = {'form':form}
    return render(request, 'StudentsApp/GetQuestionnaireList.html', context)

def ViewGetQuestionsList(request, pk):
    Get_Student_Information = CustomUserModel.objects.get(Id_User = request.user.Id_User)
    Get_Group_Information = QuestionGroupModel.objects.get(Id_QuestionGroup = pk)
    Get_Question_Information = None
    List_Of_Questions = list(QuestionsModel.objects.filter(Group_Name_Of_Quesitons=pk))
    List_Of_Options = {}
    context = {}
    wrong_answer = False
    total_marks = 0
    score = 0
    final_marks = 0

    if 'index' not in request.session or 'tries' not in request.session:
        request.session['index'] = 0
        request.session['tries'] = 2

    get_index = int(request.session['index'])
    Get_Question_Information = List_Of_Questions[get_index]
    tries = request.session.get('tries')

    if request.method == 'POST':
        selected_option = request.POST.get('Question_Option')
        question_marks = List_Of_Questions[get_index].Question_Marks

        if selected_option == "True":
            wrong_answer = False
            score += question_marks if tries == 2 else question_marks/2
            print('1: '+str(score))
            # Add Model here
            save_performance =StudentPerformance(Student_Information = Get_Student_Information, Question_Information = Get_Question_Information, Question_Group_Information = Get_Group_Information, Score_Per_Question = score)
            save_performance.save()
        if selected_option == "False":
            if tries is None:
                tries = request.session.get('tries')
                tries = 2
            tries -= 1
            request.session['tries'] = tries
            if tries == 0:
                get_index += 1
                request.session['index'] = get_index
                request.session['tries'] = 2
                if get_index >= len(List_Of_Questions):
                    save_performance =StudentPerformance(Student_Information = Get_Student_Information, Question_Information = Get_Question_Information, Question_Group_Information = Get_Group_Information, Score_Per_Question = score)
                    save_performance.save()
                    

                    return redirect('StudentsApp:ResultView')
                    return HttpResponse(f'You have got {score} out of {total_marks}')
                else:
                    List_Of_Options = MCQModel.objects.filter(Related_Question__Id_Question = List_Of_Questions[get_index].Id_Question)
                    print('2: '+str(score))
                    # Add Model Here
                    save_performance =StudentPerformance(Student_Information = Get_Student_Information, Question_Information = Get_Question_Information, Question_Group_Information = Get_Group_Information, Score_Per_Question = score)
                    save_performance.save()
                    final_marks += score
                    context = {'Question':List_Of_Questions[get_index], 'Options':List_Of_Options, 'wrong_answer':wrong_answer, 'tries': request.session.get('tries'), 'current_score':score, 'Questionnaire_Name': Get_Group_Information, 'Total_Questions': str(len(List_Of_Questions)), 'current_question':get_index, 'Total_marks':final_marks}
                    return render(request, 'StudentsApp/GetQuestionsList.html', context)
            else:
                List_Of_Options = MCQModel.objects.filter(Related_Question__Id_Question = List_Of_Questions[get_index].Id_Question)
                wrong_answer = True
                score += question_marks if tries == 2 else question_marks/2
                print('3: '+str(score))
                final_marks += score
                context = {'Question':List_Of_Questions[get_index], 'Options':List_Of_Options, 'wrong_answer':wrong_answer, 'tries': tries, 'current_score':score, 'Questionnaire_Name': Get_Group_Information, 'Total_Questions': str(len(List_Of_Questions)), 'current_question':get_index, 'Total_marks':final_marks}
                return render(request, 'StudentsApp/GetQuestionsList.html', context)


        total_marks += question_marks
        get_index += 1
        request.session['index'] = get_index
        request.session['tries'] = 2

        if get_index >= len(List_Of_Questions):
            request.session['index'] = 0
            request.session['tries'] = 2
            return redirect('StudentsApp:ResultView')
            return HttpResponse(f'No More Questions To Show')

    if get_index >= len(List_Of_Questions):
        request.session['index'] = 0
        request.session['tries'] = 2
        final_marks += score
        context = {'score': score, 'total_marks': total_marks}
        return render(request, 'StudentsApp/Result.html', context)
    else:
        List_Of_Options = MCQModel.objects.filter(Related_Question__Id_Question = List_Of_Questions[get_index].Id_Question)
        question = List_Of_Questions[get_index]
        total_marks = question.Question_Marks
        final_marks += score
        context = {'Question':question, 'Options':List_Of_Options, 'wrong_answer':wrong_answer, 'tries': request.session.get('tries'), 'current_score':score,  'Questionnaire_Name': Get_Group_Information, 'Total_Questions': str(len(List_Of_Questions)), 'current_question': str(get_index), 'Total_marks':final_marks}
        return render(request, 'StudentsApp/GetQuestionsList.html', context)
    
def ViewResult(request):
    if 'index' in request.session or 'tries' in request.session:
        del request.session['index']
        del request.session['tries']
    return render(request,'StudentsApp/Result.html')