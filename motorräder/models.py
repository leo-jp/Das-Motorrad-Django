from django.db import models

'''
    Motorräder - a collection of motorcycle brands.
'''

class Motorräder(models.Model):
    brand = models.CharField(max_length=300)
    origin = models.CharField(max_length=300)
    year = models.DateField()
    history = models.TextField()
    source = models.URLField()