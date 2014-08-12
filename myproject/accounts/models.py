from django.db import models

# Create your models here.


class Account(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created = models.DateTimeField('date created')
    view_order = models.IntegerField()
    is_default = models.BooleanField()
    is_hidden = models.BooleanField()

    def __str__(self):
        return "[{0}]".format(self.name)