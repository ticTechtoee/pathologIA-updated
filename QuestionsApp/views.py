from django.shortcuts import render, redirect
from .forms import CreateQuestionGroupForm,CreateQuestionsForm
from .models import QuestionGroupModel
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
    if request.method == 'POST':
        form = CreateQuestionsForm(request.POST or None)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'QuestionsApp/CreateQuestion.html', context)

def ViewImagesGrid(request):
    all_images = ImageModel.objects.all()
    context = {'list_of_images':all_images}
    return render(request, 'QuestionsApp/referencestemplates/ImagesGrid.html', context)

def ViewCreateOption(request):
    return render(request, 'QuestionsApp/CreateOption.html')