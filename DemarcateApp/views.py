from django.shortcuts import render, redirect
from ImagesApp.models import ImageModel
from .forms import SelectImageForm
from .models import DemarcateQuestion
from QuestionsApp.models import QuestionsModel


def ViewSelectImage(request):
    form = SelectImageForm()
    if request.method == 'POST':
        form = SelectImageForm(request.POST or None)
        form.save(commit=False)
        Image_Number = request.POST.get('Question_Image')
        return redirect('DemarcateApp:CreateDemarcateQuestionView', pk = Image_Number)
    context = {'form':form}
    return render(request, 'DemarcateApp/SelectImagePage.html', context)



def ViewCreateDemarcateQuestion(request, pk):
    Image_Instance = ImageModel.objects.get(Id_Image = pk)
    Get_Questions = QuestionsModel.objects.all()
    context = {'instance': Image_Instance, 'List_of_Questions': Get_Questions}

    if request.method == "POST":
        Width_Of_Marked_Area = request.POST.get('width')
        Height_Of_Marked_Area = request.POST.get('height')
        StartX_Of_Marked_Area = request.POST.get('startX')
        StartY_Of_Marked_Area = request.POST.get('startY')

        Total_Area = abs(int(Width_Of_Marked_Area) * int(Height_Of_Marked_Area))
        
        Question_ID = request.POST.get("Question_List")
        Question_Instance = QuestionsModel.objects.get(Id_Question=str(Question_ID))
        
        Create_Object = DemarcateQuestion(StartX = StartX_Of_Marked_Area,StartY = StartY_Of_Marked_Area,Width = Width_Of_Marked_Area ,Height = Height_Of_Marked_Area, Area = Total_Area, Question_Image = Image_Instance, Related_Question = Question_Instance)
        Create_Object.save()

    return render(request, 'DemarcateApp/demarcate.html', context)
