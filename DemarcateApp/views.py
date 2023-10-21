from django.urls import reverse
from django.shortcuts import render, redirect
from ImagesApp.models import ImageModel
from .forms import SelectImageForm, CreateDemarcateQuestionsForm,GetQuestionnaireListForm
from .models import DemarcateQuestion,DemarcateQuestionsModel
from QuestionsApp.models import QuestionGroupModel
from QuestionsApp.models import QuestionsModel
from django.http import HttpResponse
from StudentsApp.models import StudentPerformance, StudentPerfomranceInDemarcateQuizes
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
        Question_Instance = DemarcateQuestionsModel.objects.get(Id_Question=str(Question_ID))
        
        Create_Object = DemarcateQuestion(StartX = StartX_Of_Marked_Area,StartY = StartY_Of_Marked_Area,Width = Width_Of_Marked_Area ,Height = Height_Of_Marked_Area, Area = Total_Area, Question_Image = Image_Instance, Related_Question = Question_Instance)
        Create_Object.save()

        return redirect('DemarcateApp:CreateDemarcateQuestionView')

    return render(request, 'DemarcateApp/TeacherDemarcate.html', context)




"""Students Side of Demarcate Question"""

def ViewGetDemarcateQuestionnaireList(request):
    form = GetQuestionnaireListForm()
    if request.method == 'POST':
        form = GetQuestionnaireListForm(request.POST or None)
        Get_Name = request.POST.get('Name_Of_Group')
        return redirect(reverse('DemarcateApp:AnswerDemarcateQuestionView', kwargs={'pk': str(Get_Name)} ))
    context = {'form': form}
    return render(request, 'DemarcateApp/StudentSelectQuestionnaire.html', context)


def ViewAnswerDemarcateQuestion(request, pk):
    List_of_Question = list(DemarcateQuestion.objects.filter(Related_Question__Group_Name_Of_Quesitons=pk))
    Get_Student_Information = CustomUserModel.objects.get(Id_User=request.user.Id_User)
    Get_Question_Information = None
    Get_Group_Information = QuestionGroupModel.objects.get(Id_QuestionGroup=pk)

    # Initialize variables to False
    X_Range = False
    Y_Range = False
    Width_Range = False
    Height_Range = False
    Area_Range = False
    is_wrong = None  # Initialize to True

        # Set DTries to 2 if it doesn't exist in the session
    if 'DIndex' not in request.session or 'DTries' not in request.session:
        request.session['DIndex'] = 0
        request.session['DTries'] = 2

    get_index = int(request.session.get('DIndex'))
    Get_Question_Information = List_of_Question[get_index]

    get_tries = request.session.get('DTries')

    if request.method == 'POST':
        if get_index < len(List_of_Question):
 # Need To Shift this portion in a different function           
 # ---------------------------------------------------
            StartX_Of_Marked_Area = int(request.POST.get('startX'))
            StartY_Of_Marked_Area = int(request.POST.get('startY'))
            Width_Of_Marked_Area = int(request.POST.get('width'))
            Height_Of_Marked_Area =int(request.POST.get('height'))
            # Area = abs(int(Width_Of_Marked_Area) * int(Height_Of_Marked_Area))
            Threshold = 100  # Temp
            if get_index < len(List_of_Question):
                """Positive Range"""
                X_P_Range = range((List_of_Question[get_index].StartX), (List_of_Question[get_index].StartX  + Threshold), 1)
                Y_P_Range = range((List_of_Question[get_index].StartY),
                                  (List_of_Question[get_index].StartY + Threshold), 1)
                Width_P_Range = range((List_of_Question[get_index].Width),
                                      (List_of_Question[get_index].Width + Threshold), 1)
                Height_P_Range = range((List_of_Question[get_index].Height),
                                       (List_of_Question[get_index].Height + Threshold), 1)
                # Area_P_Range = range((List_of_Question[get_index].Area),
                #                      (List_of_Question[get_index].Area + Threshold), 1)

                """Negative Range"""
                X_N_Range = range((List_of_Question[get_index].StartX - Threshold),
                                  (List_of_Question[get_index].StartX), 1)
                Y_N_Range = range((List_of_Question[get_index].StartY - Threshold),
                                  (List_of_Question[get_index].StartY), 1)
                Width_N_Range = range((List_of_Question[get_index].Width - Threshold),
                                      (List_of_Question[get_index].Width), 1)
                Height_N_Range = range((List_of_Question[get_index].Height - Threshold),
                                       (List_of_Question[get_index].Height), 1)
                # Area_N_Range = range((List_of_Question[get_index].Area - Threshold),
                #                      (List_of_Question[get_index].Area), 1)

# -------------------------------------------------------------------------------------------------------------------
                print("X Positive: " + str(X_P_Range) + " or " + str(X_N_Range))
                print("Studnet X Area: " + str(StartX_Of_Marked_Area))
                print("Y Positive: " + str(Y_P_Range) + " or " + str(Y_N_Range))
                print("Studnet Y Area: " + str(StartY_Of_Marked_Area))
                print("Width: " + str(Width_P_Range) + " or " + str(Width_N_Range))
                print("Studnet Width: " + str(Width_Of_Marked_Area))

                print("Height: " + str(Height_P_Range) + " or " + str(Height_N_Range))
                print("Student Height: " + str(Height_Of_Marked_Area))

                # print("Area: " + str(Area_P_Range) + " or " + str(Area_N_Range))
                # print("Student Area: " + str(Area))
                
                # Check conditions and update variables
                if (StartX_Of_Marked_Area in list(X_P_Range)) or (StartX_Of_Marked_Area in list(X_N_Range)):
                    X_Range = True
                    print("X in Range")
                if (StartY_Of_Marked_Area in list(Y_P_Range)) or (StartY_Of_Marked_Area in list(Y_N_Range)):
                    Y_Range = True
                    print("Y in Range")
                if (Width_Of_Marked_Area in list(Width_P_Range)) or (Width_Of_Marked_Area in list(Width_N_Range)):
                    Width_Range = True
                    print("Width in Range")
                if (Height_Of_Marked_Area in list(Height_P_Range)) or (Height_Of_Marked_Area in list(Height_N_Range)):
                    Height_Range = True
                    print("Height in Range")
                # if (Area in list(Area_P_Range)) or (Area in list(Area_N_Range)):
                #     Area_Range = True
                #     print("Area in Range")

                # Check if all conditions are met
                # Area Range Removed
                if all([X_Range, Y_Range, Width_Range, Height_Range]):
                    is_wrong = False
                    print("Your Answer is Correct")
                    save_performance = StudentPerfomranceInDemarcateQuizes(
                        Student_Information=Get_Student_Information,
                        Question_Information=Get_Question_Information.Related_Question,
                        Question_Group_Information=Get_Group_Information,
                        Score_Per_Question=5.0)
                    save_performance.save()
                    get_index += 1
                    request.session['DIndex'] = get_index
                    request.session['DTries'] = 2

                    if get_index >= len(List_of_Question):
                        return redirect('DemarcateApp:ResultView')
                        return HttpResponse("No More Questions to show")
                else:
                    print("Your Answer is wrong")
                    is_wrong = True
                    if get_tries is None:
                        get_tries = request.session.get('DTries')
                        get_tries = 2
                    get_tries -= 1
                    request.session['DTries'] = get_tries
                    if get_tries == 0:
                        get_index += 1
                        request.session['DIndex'] = get_index
                        request.session['DTries'] = 2

                        if get_index >= len(List_of_Question):
                            return redirect('DemarcateApp:ResultView')
                            return HttpResponse("No More Questions to show")
               
        if get_index >= len(List_of_Question):
            request.session['DIndex'] = 0
            request.session['DTries'] = 2
            return redirect('DemarcateApp:ResultView')

            return HttpResponse("No More Questions to Show")
        
        else:
            question = List_of_Question[get_index]
            
            context = {'Demarcate_Question_List': question, 'is_wrong': is_wrong}
            return render(request, 'DemarcateApp/StudentDemarcate.html', context)


    context = {'Demarcate_Question_List': List_of_Question[get_index], 'is_wrong': is_wrong}
    return render(request, 'DemarcateApp/StudentDemarcate.html', context)


def ViewResult(request):
    if 'DIndex' in request.session or 'DTries' in request.session:
        del request.session['DIndex']
        del request.session['DTries']
    return render(request,'DemarcateApp/Result.html')