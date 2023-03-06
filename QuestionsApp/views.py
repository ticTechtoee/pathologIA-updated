from django.shortcuts import render


def ViewCreateQuestionGroup(request):
    return render(request, 'QuestionsApp/CreateQuestionsGroup.html')

def ViewCreateQuestion(request):
    return render(request, 'QuestionsApp/CreateQuestion.html')

def ViewCreateOption(request):
    return render(request, 'QuestionsApp/CreateOption.html')