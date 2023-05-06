from .models import DemarcateQuestion
from QuestionsApp.models import QuestionsModel
from ImagesApp.models import ImageModel
from django import forms



class SelectImageForm(forms.ModelForm):
    Question_Image = forms.ModelChoiceField(required=False, queryset=ImageModel.objects.all(), label="", empty_label="Selecione o número da imagem", widget=forms.Select(attrs={'class': 'custom-select'}))
    class Meta:
        model = DemarcateQuestion
        fields = ['Question_Image']
        exclude = ['StartX','StartY','Width','Height','Area','Related_Question']