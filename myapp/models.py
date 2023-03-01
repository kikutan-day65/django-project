from django.db import models

# this file is used to create and manage database
# Create your models here.

class Feature:
    id: int
    name: str
    detail: str
    is_true: bool