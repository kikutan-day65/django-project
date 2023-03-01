from django.db import models

# this file is used to create and manage database
# Create your models here.

"""
    if you created new models, follow these steps below:
        1. py manage.py makemigrations 
        2. py manage.py migrate
"""


class Feature(models.Model):
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=500)