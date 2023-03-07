from django.db import models
import uuid
import math

# Demarcte Questions or MCQS!
class QuestionTypesModel(models.Model):
    Id_Type_Question = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Category = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.Category

class QuestionsModel(models.Model):
    Id_Question = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Question_Number = models.PositiveIntegerField(blank=True, null=True)
    Question_Text = models.CharField(max_length=1000, blank=True, null=True)
    Question_Marks = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Correct_Answer = models.CharField(max_length=1, blank=True, null=True, default="A")
    Type_Of_Question = models.ForeignKey('QuestionTypesModel', models.DO_NOTHING, verbose_name="Type of Question", blank=True, null=True)
    Group_Name_Of_Quesitons = models.ForeignKey('QuestionGroupModel', models.DO_NOTHING, verbose_name="Group Name of Subject", blank=True, null=True)
    Video_For_Quesiton = models.ForeignKey('VideosApp.VideoModel', models.DO_NOTHING, verbose_name="Link Video", blank=True, null=True)
    Image_For_Quesiton = models.ForeignKey('ImagesApp.ImageModel', models.DO_NOTHING, verbose_name="Link Image", blank=True, null=True)
    
    def __str__(self):
        return self.Question_Text
    
    @classmethod
    def create(cls, **kwargs):
        # generate the question_number value
        last_question = cls.objects.last()
        if last_question:
            last_number = int(last_question.question_number.split('-')[-1])
            question_number = f"Q-{last_number+1:05}"
        else:
            question_number = "Q-00001"
            
        # create the new question object
        return cls.objects.create(Question_Number=question_number, **kwargs)


class QuestionGroupModel(models.Model):
    def number():
        no = QuestionGroupModel.objects.count()
        if no == None:
            return 1
        else:
            return no + 1
        
    Id_QuestionGroup = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Group_Number = models.IntegerField(unique=True, default=number)
    Name_Of_Group = models.CharField(max_length=150, blank=True, null=True)
    Subject_Description = models.CharField(max_length=250, blank=True, null=True)
    Date_Of_Creation = models.DateField(blank=True, null=True)
    Online_Status = models.IntegerField(blank=True, null=True)
    Creators_Information = models.ForeignKey('AccountsApp.CustomUserModel', models.DO_NOTHING, blank=True, null=True)
    def __str__(self):
        return self.Name_Of_Group

class MCQModel(models.Model):
    Id_MCQs = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Option = models.CharField(max_length=1, blank=True, null=True)
    Option_Text = models.CharField(max_length=1000, blank=True, null=True)
    Related_Question = models.ForeignKey('QuestionsModel', models.DO_NOTHING, verbose_name="Related Question")

    def __str__(self):
        return self.Option_Text