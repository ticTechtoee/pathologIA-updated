# from django.db import models
# import uuid

# class ResultModel(models.Model):
#     idresult = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
#     iduser_user = models.ForeignKey('accounts.User', models.DO_NOTHING, db_column='usuario_idusuario', blank=True, null=True)
#     quiz_quiz_id = models.ForeignKey('Questionnaire', models.DO_NOTHING, db_column='questionario_idquestionario', blank=True, null=True)
#     descriptiondate = models.DateTimeField(blank=True, null=True)
#     total = models.DecimalField(max_digits=10, decimal_places=2)
