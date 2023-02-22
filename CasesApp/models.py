from django.db import models
import uuid

class CasesModel(models.Model):
    idcase = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    descricao = models.CharField(max_length=1000, blank=True, null=True)
    imageidimage = models.ForeignKey('images.Image', models.DO_NOTHING, db_column='imagemidimagem', blank=True, null=True)
    # This Needs to be Discussed
    this_question = models.ForeignKey('Questions', models.DO_NOTHING, db_column='questoesidquestao')
    useriduser = models.ForeignKey('accounts.User', models.DO_NOTHING, db_column='usuarioidusuario', blank=True, null=True)

    class Meta:
        db_table = 'cases'

