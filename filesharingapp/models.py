from django.db import models

# Create your models here.
class file(models.Model):
    filename=models.CharField(max_length=20)
    filetypedata=models.FileField(upload_to='media/')

class upload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    filedata = models.FileField()

    def delete(self, *args, **kwargs):
        self.filedata.delete()
        super().delete(*args, **kwargs)