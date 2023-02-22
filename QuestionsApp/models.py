from django.db import models
import uuid

# Demarcte Questions or MCQS!
class QuestionTypesModel(models.Model):
    Id_Type_Question = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Category = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.Category

class QuestionsModel(models.Model):
    Id_Question = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Question_Number = models.IntegerField(unique=True, editable=False)
    Question_Text = models.CharField(max_length=1000, blank=True, null=True)
    Question_Marks = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Correct_Answer = models.CharField(max_length=1, blank=True, null=True, default="A")
    Type_Of_Question = models.ForeignKey('QuestionTypesModel', models.DO_NOTHING, verbose_name="Type of Question", blank=True, null=True)
    Group_Name_Of_Quesitons = models.ForeignKey('QuestionGroupModel', models.DO_NOTHING, verbose_name="Group Name of Subject", blank=True, null=True)
    Video_For_Quesiton = models.ForeignKey('VideosApp.VideoModel', models.DO_NOTHING, verbose_name="Link Video", blank=True, null=True)
    Image_For_Quesiton = models.ForeignKey('ImagesApp.ImageModel', models.DO_NOTHING, verbose_name="Link Image", blank=True, null=True)
    
    def __str__(self):
        return self.Question_Text
    
    def save(self, *args, **kwargs):
        if not self.pk:
            last_obj = QuestionsModel.objects.all().order_by('-number').first()
            if last_obj:
                self.number = last_obj.number + 1
            else:
                self.number = 1
        super().save(*args, **kwargs)


class QuestionGroupModel(models.Model):
    Id_QuestionGroup = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Name_Of_Group = models.CharField(max_length=150, blank=True, null=True)
    Subject_Description = models.CharField(max_length=250, blank=True, null=True)
    Date_Of_Creation = models.DateTimeField(blank=True, null=True)
    Online_Status = models.IntegerField(blank=True, null=True)
    #Co Educator This Feild needs to be addressed
    Creators_Information = models.ForeignKey('AccountsApp.CustomUserModel', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.Name_Of_Group

#MCQS Option
class MCQModel(models.Model):
    Id_MCQs = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Option = models.CharField(max_length=1, blank=True, null=True)
    Option_Text = models.CharField(max_length=1000, blank=True, null=True)
    Related_Question = models.ForeignKey('QuestionsModel', models.DO_NOTHING, verbose_name="Related Question")

    def __str__(self):
        return self.Option_Text