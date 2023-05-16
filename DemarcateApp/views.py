from django.shortcuts import render, redirect
from ImagesApp.models import ImageModel
from .forms import SelectImageForm, CreateDemarcateQuestionsForm
from .models import DemarcateQuestion,DemarcateQuestionsModel
from QuestionsApp.models import QuestionsModel
from django.http import HttpResponse
from StudentsApp.models import StudentPerformance
from AccountsApp.models import CustomUserModel




"""Teacher's Side of Demarcate Question"""
def ViewCreateDemarcateQuestion(request):
    form = CreateDemarcateQuestionsForm()
    if request.method == 'POST':
        form = CreateDemarcateQuestionsForm(request.POST or None)
        form.save()
        return redirect('DemarcateApp:SelectImageView')
    context = {'form':form}
    return render(request, 'DemarcateApp/CreateQuestion.html', context)

def ViewSelectImage(request):
    form = SelectImageForm()
    if request.method == 'POST':
        form = SelectImageForm(request.POST or None)
        form.save(commit=False)
        Image_Number = request.POST.get('Question_Image')
        return redirect('DemarcateApp:CreateDemarcateAreaView', pk = Image_Number)
    context = {'form':form}
    return render(request, 'DemarcateApp/SelectImagePage.html', context)

def ViewCreateDemarcateArea(request, pk):
    Image_Instance = ImageModel.objects.get(Id_Image = pk)
    Get_Questions = DemarcateQuestionsModel.objects.all()
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

    return render(request, 'DemarcateApp/TeacherDemarcate.html', context)




"""Students Side of Demarcate Question"""
def ViewAnswerDemarcateQuestion(request):
    List_of_Question = list(DemarcateQuestion.objects.all())
    Get_Student_Information = CustomUserModel.objects.get(Id_User = request.user.Id_User)
    Get_Question_Information = None

    
    if 'Dindex' not in request.session:
        request.session['Dindex'] = 0
    
    get_index = int(request.session['Dindex'])

    if request.method == 'POST':
        if get_index < len(List_of_Question):
            Get_Question_Information = List_of_Question[get_index]
            get_index += 1
            request.session['Dindex'] = get_index
            
            StartX_Of_Marked_Area = request.POST.get('startX')
            StartY_Of_Marked_Area = request.POST.get('startY')
            Width_Of_Marked_Area = request.POST.get('width')
            Height_Of_Marked_Area = request.POST.get('height')

            Area = abs(int(Width_Of_Marked_Area) * int(Height_Of_Marked_Area))

            Threshold = 30

            X_Range = range((List_of_Question[get_index].StartX - Threshold),(List_of_Question[get_index].StartX),1)
            Y_Range = range((List_of_Question[get_index].StartY - Threshold),(List_of_Question[get_index].StartY),1)
            Width_Range = range((List_of_Question[get_index].Width - Threshold),(List_of_Question[get_index].Width),1)
            Height_Range = range((List_of_Question[get_index].Height - Threshold),(List_of_Question[get_index].Height),1)
            Area_Range = range((List_of_Question[get_index].Area - Threshold),(List_of_Question[get_index].Area),1)
            if (StartX_Of_Marked_Area in X_Range) and (StartY_Of_Marked_Area in Y_Range) and (Width_Of_Marked_Area in Width_Range) and (Height_Of_Marked_Area in Height_Range) and (Area in Area_Range):
                print("Your Answer is Correct")
                save_performance = StudentPerformance(Student_Information = Get_Student_Information, Question_Information = Get_Question_Information, Question_Group_Information = Get_Group_Information, Score_Per_Question = 5.0)
                save_performance.save()
            else:
                print("Your Answer is wrong")
                save_performance = StudentPerformance(Student_Information = Get_Student_Information, Question_Information = Get_Question_Information, Question_Group_Information = Get_Group_Information, Score_Per_Question = 0.0)
                save_performance.save()
            if get_index < len(List_of_Question):
                context = {'Demarcate_Question_List':List_of_Question[get_index] }
                return render(request, 'DemarcateApp/StudentDemarcate.html', context)
            else:
                print('No More Questions To Show')
                request.session['Dindex'] = 0
                return HttpResponse('No More Questions To Show')


    context = {'Demarcate_Question_List':List_of_Question[0] }
    return render(request, 'DemarcateApp/StudentDemarcate.html', context)
