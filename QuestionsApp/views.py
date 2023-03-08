from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CreateQuestionGroupForm,CreateQuestionsForm,EditQuestionsForm
from .models import QuestionGroupModel, QuestionsModel
from ImagesApp.models import ImageModel


def ViewCreateQuestionGroup(request):
    Questionnaire_Objects = QuestionGroupModel.objects.filter(Creators_Information = request.user)

    form = CreateQuestionGroupForm()
    if request.method == 'POST':
        form = CreateQuestionGroupForm(request.POST or None)
        if form.is_valid():
            ins = form.save(commit=False)
            
            Status = request.POST.get('status')
            ins.Online_Status = Status

            Creator = request.user
            ins.Creators_Information = Creator

            ins.save()
            return redirect('QuestionsApp:CreateQuestionView')
        else:
            print(form.errors)
    context = {'form':form, 'Questionnaire_Information': Questionnaire_Objects}
    return render(request, 'QuestionsApp/CreateQuestionsGroup.html', context)

def ViewEditQuestionGroup(request, pk):
    question_obj = QuestionGroupModel.objects.get(Id_QuestionGroup = pk)
    form = CreateQuestionGroupForm(instance=question_obj)
    if request.method == 'POST':
        form = CreateQuestionGroupForm(request.POST, instance=question_obj)
        if form.is_valid():
            form.save()
            return redirect('QuestionsApp:CreateQuestionGroupView')
    context = {'form':form}
    return render(request, 'QuestionsApp/CreateQuestionsGroup.html', context)

def ViewDeleteQuestionGroup(request, pk):
    question_obj = QuestionGroupModel.objects.get(Id_QuestionGroup = pk)
    question_obj.delete()
    return redirect('QuestionsApp:CreateQuestionGroupView')


def ViewCreateQuestion(request):
    form = CreateQuestionsForm()
    editForm = EditQuestionsForm()
    if request.method == 'POST':
        if 'editButton' in request.POST:
            editForm = EditQuestionsForm(request.POST or None)
            get_question_number = request.POST.get('Question_Number')
            return redirect(reverse('QuestionsApp:EditQuestionView', kwargs={'question_number': str(get_question_number)} ))
        elif 'deleteButton' in request.POST:
            editForm = EditQuestionsForm(request.POST or None)
            get_question_number = request.POST.get('Question_Number')
            return redirect(reverse('QuestionsApp:DeleteQuestionView', kwargs={'question_number': str(get_question_number)} ))
        else:
            form = CreateQuestionsForm(request.POST or None)
            if form.is_valid():
                form.save()
                return redirect('QuestionsApp:CreateQuestionView')
    context = {'form':form, 'eidtform':editForm}
    return render(request, 'QuestionsApp/CreateQuestion.html', context)

def ViewEditQuestion(request,question_number):
    question_obj = QuestionsModel.objects.get(Question_Number = question_number)
    form = CreateQuestionsForm(instance=question_obj)
    if request.method == 'POST':
        form = CreateQuestionsForm(request.POST or None, instance=question_obj)
        if form.is_valid():
            form.save()
            return redirect('QuestionsApp:CreateQuestionView')
    context={'form':form}
    return render(request,'QuestionsApp/CreateQuestion.html', context)

def ViewDeleteQuestion(request, question_number):
    question_to_delete = QuestionsModel.objects.get(Question_Number = question_number)
    question_to_delete.delete()
    return redirect('QuestionsApp:CreateQuestionView')

def ViewImagesGrid(request):
    all_images = ImageModel.objects.all()
    context = {'list_of_images':all_images}
    return render(request, 'QuestionsApp/referencestemplates/ImagesGrid.html', context)

def ViewCreateOption(request):
    return render(request, 'QuestionsApp/CreateOption.html')