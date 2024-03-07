from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
    created = models.DateField(
        'criado em',
        auto_now_add=True,
        auto_now=False
    )
    modifie = models.DateTimeField(
        'modificado em',
        auto_now_add=False,
        auto_now=True
    )
    class Meta:
        abstract = True