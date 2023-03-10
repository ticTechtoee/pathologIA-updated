from django.shortcuts import render, redirect
from QuestionsApp.models import QuestionsModel
from .forms import GetQuestionnaireListForm
from django.urls import reverse


def ViewGetQuestionnaireList(request):
    form = GetQuestionnaireListForm()
    if request.method == 'POST':
        get_questionnaire_id = request.POST.get('Name_Of_Group')
        return redirect(reverse('StudentsApp:GetQuestionsListView', kwargs = {'pk':str(get_questionnaire_id)}))
    context = {'form':form}
    return render(request, 'StudentsApp/GetQuestionnaireList.html', context)

def ViewGetQuestionsList(request, pk):
    List_Of_Questions = QuestionsModel.objects.filter(Group_Name_Of_Quesitons=pk)
    # create a dictionary to store each question and its related options
    questions_with_options = {}
    for question in List_Of_Questions:
        options = question.mcqmodel_set.all()
        questions_with_options[question] = options
    
    context = {
        'questions_with_options': questions_with_options,
    }
    
    return render(request, 'StudentsApp/GetQuestionsList.html', context)