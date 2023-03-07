from .models import QuestionGroupModel
from django import forms

STATUS = [
        ('0', 'Aberto'),
        ('1', 'Fechado'),
        ]
class CreateQuestionGroupForm(forms.ModelForm):
    
    Name_Of_Group = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'id':'cTitQuiz','name':'tTitQuiz', 'placeholder':'Título do questionário'}))
    Subject_Description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id':'cAssQuiz','name':'tAssQuiz', 'placeholder':'Descrição do assunto do questionário'}))
    class Meta:
        model = QuestionGroupModel
        fields = ['Name_Of_Group','Subject_Description','Date_Of_Creation','Online_Status']
        exclude = ['Group_Number','Creators_Information','Online_Status']
        widgets = {
            'Date_Of_Creation': forms.DateInput(format=('%Y-%m-%d'),
                                                attrs={'class': 'form-control', 
               'id':'cIdDataQuiz',
               'name':'tIdDataQuiz',
               'placeholder':'Data do cadastro do Questionário',
               'type': 'date'
              }),}
