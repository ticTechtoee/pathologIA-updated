from .models import QuestionGroupModel,QuestionsModel
from VideosApp.models import VideoModel
from ImagesApp.models import ImageModel
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

class CreateQuestionsForm(forms.ModelForm):
    Group_Name_Of_Quesitons = forms.ModelChoiceField(queryset=QuestionGroupModel.objects.all(),label="", empty_label="Selecione o Questionário", widget=forms.Select(attrs={'class': 'custom-select'}))
    Question_Text = forms.CharField(max_length=50, widget=forms.Textarea(attrs={'class': 'form-control', 'rows':'5', 'id':'cDesc','name':'tDesc', 'placeholder':'Descrição do assunto do questionário'}))
    Question_Marks = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'type':'number','min':'0','value':'1', 'step':'0.5', 'id':'cIdPeso','name':'tIdPeso', 'placeholder':'0.00'}))
    Image_For_Question = forms.ModelChoiceField(required=False, queryset=ImageModel.objects.all(), label="", empty_label="Selecione o número da imagem", widget=forms.Select(attrs={'class': 'custom-select'}))
    Video_For_Question = forms.ModelChoiceField(required=False,queryset=VideoModel.objects.all(), label="", empty_label="Selecione o número do vídeo", widget=forms.Select(attrs={'class': 'custom-select'}))
    class Meta:
        model = QuestionsModel
        fields = ['Question_Text', 'Question_Marks', 'Group_Name_Of_Quesitons']
        exclude = ['Id_Question','Image_For_Question','Video_For_Question','Question_Number', 'Type_Of_Question']