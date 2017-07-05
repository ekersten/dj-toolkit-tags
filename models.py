from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Taggable(models.Model):
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        abstract = True
