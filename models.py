from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Taggable(models.Model):
    tags = models.ForeignKey(Tag, blank=True)

    class Meta:
        abstract = True
