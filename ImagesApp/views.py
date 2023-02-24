from django.shortcuts import render
from .forms import CreateImageForm

def ViewIndex(request):
    form = CreateImageForm(request.POST or None)
    if request.method == 'POST':
        form = CreateImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'ImagesApp/Index.html', context) 
