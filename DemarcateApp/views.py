from django.shortcuts import render
from ImagesApp.models import ImageModel


def ViewCreateDemarcateQuestion(request):
    Image_Instance = ImageModel.objects.get(Image_Number = "2")
    context = {'instance': Image_Instance}

    if request.method == "POST":
        Width_Of_Marked_Area = request.POST.get('width')
        Height_Of_Marked_Area = request.POST.get('height')
        StartX_Of_Marked_Area = request.POST.get('startX')
        StartY_Of_Marked_Area = request.POST.get('startY')

        Area = abs(int(Width_Of_Marked_Area) * int(Height_Of_Marked_Area))

        print(Area)

    return render(request, 'DemarcateApp/demarcate.html', context)
