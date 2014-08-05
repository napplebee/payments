from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200)
<<<<<<< HEAD
    created = models.DateTimeField('date created')

    def __str__(self):
        return "[{0}]".format(self.name)
=======
    created = models.DateTimeField('date created')
>>>>>>> 28b9de76079fa6991abd2d86254f27cd715ed890
