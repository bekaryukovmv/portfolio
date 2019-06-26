from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'
