from django.shortcuts import render

def ViewPredictTuberclousis(request):
    return render(request,'PredictionApp/tuberculose/index.html')