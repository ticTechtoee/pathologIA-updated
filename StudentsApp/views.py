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

# def ViewGetQuestionsList(request, pk):
#     List_Of_Questions = QuestionsModel.objects.filter(Group_Name_Of_Quesitons=pk)
#     # create a dictionary to store each question and its related options
#     questions_with_options = {}
#     for question in List_Of_Questions:
#         options = question.mcqmodel_set.all()
#         questions_with_options[question] = options
    
#     context = {
#         'questions_with_options': questions_with_options,
#     }
    
#     return render(request, 'StudentsApp/GetQuestionsList.html', context)

# def ViewGetQuestionsList(request, pk):
#     List_Of_Questions = QuestionsModel.objects.filter(Group_Name_Of_Quesitons=pk)
    
#     # create a dictionary to store each question and its related options
#     questions_with_options = {}
#     for question in List_Of_Questions:
#         options = question.mcqmodel_set.all()
#         questions_with_options[question] = options
       
#     current_question_id = request.POST.get('question_id')
#     current_question_index = 0
#     next_question_index = 1
#     next_question_id = None
    
#     # Find the index of the current question in the list of questions
#     for index, question in enumerate(List_Of_Questions):
#         if str(question.Id_Question) == current_question_id:
#             current_question_index = index
#             break
    
#     # Check if there is a next question
#     if current_question_index + 1 < len(List_Of_Questions):
#         next_question_id = str(List_Of_Questions[current_question_index + 1].Id_Question)
    
#     # Get the current question and its options
#     current_question = List_Of_Questions[current_question_index]
#     current_question_options = questions_with_options[current_question]        
    
#     context = {
#         'current_question': current_question,
#         'current_question_options': current_question_options,
#         'next_question_id': next_question_id,
#     }
    
#     return render(request, 'StudentsApp/GetQuestionsList.html', context)

# def ViewGetQuestionsList(request, pk):
#     List_Of_Questions = list(QuestionsModel.objects.filter(Group_Name_Of_Quesitons=pk))
#     List_Of_Options = {}
#     wrong_answer = None
#     context = {}

#     if not request.session.has_key('index'):
#         request.session['index'] = 0
#     else:
#         get_index = int(request.session['index'])
#         if request.method == 'POST':
#             get_index = get_index + 1
#             request.session['index'] = get_index
            
#             selected_option = request.POST.get('Question_Option')
#             if selected_option == "True":
#                 print('Your Answer is right')
#             elif selected_option == "False":
                
#                 print('Your Answer is wrong')
#                 List_Of_Questions = List_Of_Questions[get_index - 1]
#                 List_Of_Options = MCQModel.objects.filter(Related_Question__Id_Question = List_Of_Questions.Id_Question)
#                 wrong_answer = True
#                 context = {'Question':List_Of_Questions, 'Options':List_Of_Options, 'wrong_answer':wrong_answer}
                
#                 return render(request, 'StudentsApp/GetQuestionsList.html', context)


#             if not get_index < len(List_Of_Questions):
#                 request.session['index'] = 0
#                 return HttpResponse('No More Questions')
#     print(get_index)                        
#     List_Of_Questions = List_Of_Questions[get_index]
#     List_Of_Options = MCQModel.objects.filter(Related_Question__Id_Question = List_Of_Questions.Id_Question)
#     context = {'Question':List_Of_Questions, 'Options':List_Of_Options, 'wrong_answer':wrong_answer}
#     return render(request, 'StudentsApp/GetQuestionsList.html', context) 

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
                    return HttpResponse(f'You have got {score} out of {total_marks}')
                else:
                    List_Of_Options = MCQModel.objects.filter(Related_Question__Id_Question = List_Of_Questions[get_index].Id_Question)
                    print('2: '+str(score))
                    # Add Model Here
                    save_performance =StudentPerformance(Student_Information = Get_Student_Information, Question_Information = Get_Question_Information, Question_Group_Information = Get_Group_Information, Score_Per_Question = score)
                    save_performance.save()
                    context = {'Question':List_Of_Questions[get_index], 'Options':List_Of_Options, 'wrong_answer':wrong_answer, 'tries': request.session.get('tries')}
                    return render(request, 'StudentsApp/GetQuestionsList.html', context)
            else:
                List_Of_Options = MCQModel.objects.filter(Related_Question__Id_Question = List_Of_Questions[get_index].Id_Question)
                wrong_answer = True
                score += question_marks if tries == 2 else question_marks/2
                print('3: '+str(score))
                context = {'Question':List_Of_Questions[get_index], 'Options':List_Of_Options, 'wrong_answer':wrong_answer, 'tries': tries}
                return render(request, 'StudentsApp/GetQuestionsList.html', context)


        total_marks += question_marks
        get_index += 1
        request.session['index'] = get_index
        request.session['tries'] = 2

        if get_index >= len(List_Of_Questions):
            request.session['index'] = 0
            request.session['tries'] = 2
            return HttpResponse(f'No More Questions To Show')
            return render(request, 'StudentsApp/Result.html', context)

    if get_index >= len(List_Of_Questions):
        request.session['index'] = 0
        request.session['tries'] = 2
        context = {'score': score, 'total_marks': total_marks}
        return render(request, 'StudentsApp/Result.html', context)
    else:
        List_Of_Options = MCQModel.objects.filter(Related_Question__Id_Question = List_Of_Questions[get_index].Id_Question)
        question = List_Of_Questions[get_index]
        total_marks = question.Question_Marks
        context = {'Question':question, 'Options':List_Of_Options, 'wrong_answer':wrong_answer, 'tries': request.session.get('tries')}
        return render(request, 'StudentsApp/GetQuestionsList.html', context)








def ViewSubmitAnswers(request, pk):
    if request.method == 'POST':
        questions_with_options = request.POST.dict()
        questions_with_options.pop('csrfmiddlewaretoken', None)
        group = QuestionGroupModel.objects.get(Id_QuestionGroup=pk)
        total_score = 0
        print('Starting for loop')
        print(questions_with_options)
        for question, selected_option in questions_with_options.items():
            print(f'Question: {question}, Selected Option: {selected_option}')
            question = QuestionsModel.objects.get(Id_Question=question.Id_Question, Group_Name_Of_Quesitons=pk)
            correct_option = question.mcqmodel_set.get(Is_Right=True)
            tries = 0
            score = 0
            while tries < 2:
                if selected_option == correct_option.Option_Text:
                    # correct answer
                    score += question.Question_Marks
                    break
                else:
                    # wrong answer
                    tries += 1
                    if tries >= 2:
                        score = 0
                        break
                    else:
                        score -= question.Question_Marks / 2
            total_score += score
            performance = StudentPerformance(
                Student_Information=request.user,
                Question_Information=question,
                Question_Group_Information=group,
                Score=score,
            )
            performance.save()

            # Get the next question ID
        current_question_id = request.POST.get('current_question_id')
        next_question = QuestionsModel.objects.filter(
            Group_Name_Of_Quesitons=pk,
            Id_Question__gt=current_question_id
        ).order_by('Id_Question').first()
        if next_question:
            next_question_id = next_question.Id_Question

        return JsonResponse({'next_question_id': next_question_id})
    else:
        return HttpResponseBadRequest('Invalid Request')
