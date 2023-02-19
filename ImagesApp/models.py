from django.db import models
import uuid

class ImageModel(models.Model):
    Id_Image = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Path_To_Folder = models.CharField(max_length=250, blank=True, null=True)
    Upload_Image = models.ImageField(upload_to='question_images/', null=True, blank=True)
    Type_Of_Image = models.ForeignKey('ImageTypeModel', models.DO_NOTHING, blank=True, null=True)
    Image_Group = models.ForeignKey('ImageGroupModel', verbose_name="Group To Which This Image Belongs To", on_delete=models.DO_NOTHING, blank=True, null=True)
    def __str__(self):
        return self.Type_Of_Image
    
class ImageTypeModel(models.Model):
    Id_Type_Image = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Description = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.Description

class ImageGroupModel(models.Model):
    Id_Group = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Description = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.Description

class ImagesQuestionsModel(models.Model):
    Id_Images_Questions = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Id_Image = models.ForeignKey(ImageModel, models.DO_NOTHING, blank=True, null=True)
    def __str__(self):
            return self.Id_Image
