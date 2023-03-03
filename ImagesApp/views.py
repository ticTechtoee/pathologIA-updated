from django.shortcuts import render, redirect, reverse
from .forms import CreateImageForm,DeleteImageForm
from .models import ImageGroupModel,ImageModel

def ViewCreateImage(request):
    form = CreateImageForm(request.POST or None)
    deleteForm = DeleteImageForm(request.POST or None)
    if request.method == 'POST':
        if 'btnSubmitFormDelete' in request.POST:
            if deleteForm.is_valid():
                group_name = deleteForm.cleaned_data.get('Image_Group')
                print(group_name)
                return redirect(reverse('ImagesApp:GridImages', kwargs={'pk': group_name}))
        elif 'btnSubmitFormEdit' in request.POST:
            if deleteForm.is_valid():
                group_name = deleteForm.cleaned_data.get('Image_Group')
                print(group_name)
                return redirect(reverse('ImagesApp:GridImages', kwargs={'pk': group_name}))
        else:
            form = CreateImageForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
    context = {'form': form, 'delteImageform':deleteForm}
    return render(request, 'ImagesApp/Index.html', context) 


def ViewImagesGrid(request, pk):
    selected_group = ImageGroupModel.objects.get(Description=str(pk))
    selected_group_images = ImageModel.objects.filter(Image_Group=selected_group.Id_Group)
    context = {'list_of_images':selected_group_images}
    return render(request, 'ImagesApp/ImagesGrid.html', context)

def ViewDeleteImage(request, pk):
    image_to_delete = ImageModel.objects.get(Id_Image = str(pk))
    image_to_delete.delete()
    return redirect('ImagesApp:CreateImageView') 

def ViewEditImage(request,pk):
    image_obj = ImageModel.objects.get(Id_Image = pk)
    form = CreateImageForm(instance=image_obj)
    if request.method == 'POST':
        form = CreateImageForm(request.POST, request.FILES, instance=image_obj)
        if form.is_valid():
            form.save()
            return redirect('ImagesApp:CreateImageView')
    context = {'form':form}
    return render(request, 'ImagesApp/Index.html', context)