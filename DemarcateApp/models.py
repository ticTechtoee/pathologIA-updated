from django.db import models
import uuid


# Create your models here.
class DemarcateQuestion(models.Model):
    Id_Marked = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    StartX = models.IntegerField(blank=True, null=True)
    StartY = models.IntegerField(blank=True, null=True)
    Width = models.IntegerField(blank=True, null=True)
    Height = models.IntegerField(blank=True, null=True)
    Area = models.IntegerField(blank=True, null=True)
    Question_Image = models.ForeignKey('ImagesApp.ImageModel', models.DO_NOTHING, verbose_name="Link Image", blank=True, null=True)
    Related_Question = models.ForeignKey('QuestionsApp.QuestionsModel', models.DO_NOTHING, verbose_name="Related Question")

    def __str__(self):
        return self.Related_Question