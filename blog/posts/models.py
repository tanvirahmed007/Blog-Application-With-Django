from django.db import models
from datetime import datetime
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
    created_at = models.DateField(default = datetime.now, blank = True)
