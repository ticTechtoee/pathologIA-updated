from django.shortcuts import render
from .forms import CreateQuestionGroupForm


def ViewCreateQuestionGroup(request):
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
        else:
            print(form.errors)
    context = {'form':form}
    return render(request, 'QuestionsApp/CreateQuestionsGroup.html', context)

def ViewCreateQuestion(request):
    return render(request, 'QuestionsApp/CreateQuestion.html')

def ViewCreateOption(request):
    return render(request, 'QuestionsApp/CreateOption.html')