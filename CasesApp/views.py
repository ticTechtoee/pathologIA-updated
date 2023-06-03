from django.shortcuts import render, redirect
from .forms import CasesForm
from .models import CasesModel

def ViewUploadFile(request):
    if request.method == 'POST':
        form = CasesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return redirect('search_pdf')
    else:
        form = CasesForm()
    
    return render(request, 'CasesApp/casos.html', {'form': form})

def search_pdf(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        results = CasesModel.objects.filter(CaseStudyFileName__icontains=search_query)
    else:
        results = CasesModel.objects.all()
    
    return render(request, 'search_pdf.html', {'results': results})
