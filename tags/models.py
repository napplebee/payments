from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField('date created')

    def __str__(self):
        return "[{0}]".format(self.name)