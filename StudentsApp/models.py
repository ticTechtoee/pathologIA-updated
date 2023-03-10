from django.db import models
import uuid

# # Create your models here.
# class Result(models.Model):
#     idresult = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
#     iduser_user = models.ForeignKey('accounts.User', models.DO_NOTHING, db_column='usuario_idusuario', blank=True, null=True)
#     quiz_quiz_id = models.ForeignKey('Questionnaire', models.DO_NOTHING, db_column='questionario_idquestionario', blank=True, null=True)
#     descriptiondate = models.DateTimeField(blank=True, null=True)
#     total = models.DecimalField(max_digits=10, decimal_places=2)

# class QuestionPerformance(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     #student = models.ForeignKey(User, on_delete=models.CASCADE)
#     #question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     answer = models.CharField(max_length=1000)
#     score = models.DecimalField(max_digits=10, decimal_places=2)
#     #created_at = models.DateTimeField(default=timezone.now)
#     #question_group = models.ForeignKey(QuestionGroupModel, on_delete=models.CASCADE)

# #     def __str__(self):
#         return f"{self.student.username}'s performance on question {self.question.question_number} in group {self.question_group.Name_Of_Group}"