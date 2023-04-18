from django.db import models
import uuid
from django.utils import timezone
from QuestionsApp.models import QuestionGroupModel


class StudentPerformance(models.Model):
    StudentPerformance_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Student_Information = models.ForeignKey('AccountsApp.CustomUserModel', on_delete=models.DO_NOTHING)
    Question_Information = models.ForeignKey('QuestionsApp.QuestionsModel', on_delete=models.DO_NOTHING)
    #Question_Group_Information = models.ForeignKey('QuestionsApp.QuestionGroupModel', on_delete=models.DO_NOTHING, default=QuestionGroupModel.objects.first().pk)
    Score_Per_Question = models.DecimalField(max_digits=10, decimal_places=2)
    Completed_At = models.DateTimeField(auto_now_add=True)
