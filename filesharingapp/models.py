from django.db import models

from filesharingapp.storage_backends import PublicMediaStorage, PrivateMediaStorage
# Create your models here.
class file(models.Model):
    filename=models.CharField(max_length=20)
    filetypedata=models.FileField()

class upload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    filedata = models.FileField(storage=PublicMediaStorage())

    def delete(self, *args, **kwargs):
        self.filedata.delete()
        super().delete(*args, **kwargs)


class uploadPrivate(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    filedata = models.FileField(storage=PrivateMediaStorage())

    def delete(self, *args, **kwargs):
        self.filedata.delete()
        super().delete(*args, **kwargs)